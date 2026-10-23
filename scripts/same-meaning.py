#!/usr/bin/env python3
"""Prints what each given page lost or added since a base commit, and exits 1 when it lost something."""
from __future__ import annotations

import os
import re
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

GROWTH_CAP = 0.10
LIMITING_WORDS = ("never", "not", "only", "unless", "except")
NUMBER_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
    "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14", "fifteen": "15",
    "sixteen": "16", "seventeen": "17", "eighteen": "18", "nineteen": "19", "twenty": "20",
    "thirty": "30", "forty": "40", "fifty": "50", "hundred": "100",
}

CODE_SPAN = re.compile(r"`[^`\n]+`")
RULE_CITATION = re.compile(r"\*\*rule-[a-z0-9-]+\*\*")
PLUGIN_PATH = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/[A-Za-z0-9_./-]+")
NUMBER = re.compile(r"\b(?:\d{1,3}(?:,\d{3})+|\d+|" + "|".join(NUMBER_WORDS) + r")\b", re.IGNORECASE)
QUOTED = re.compile(r"\"([^\"\n]+)\"|“([^”\n]+)”")
BOLD = re.compile(r"\*\*[^*\n]+\*\*")
STEP_REFERENCE = re.compile(r"\b(?:steps?|stop)\s+\d+\b", re.IGNORECASE)
LIMITING_WORD = re.compile(r"\b(?:" + "|".join(LIMITING_WORDS) + r")\b", re.IGNORECASE)


@dataclass(frozen=True)
class Kind:
    name: str
    items: Callable[[str], list[str]]


@dataclass(frozen=True)
class Difference:
    kind: str
    item: str
    lost: bool


@dataclass(frozen=True)
class Report:
    differences: tuple[Difference, ...]
    headings_changed: bool
    warnings: tuple[str, ...]

    @property
    def lost_something(self) -> bool:
        return self.headings_changed or any(difference.lost for difference in self.differences)


def prose(text: str) -> str:
    """The text with each code span blanked, so its quotes, stars and digits are not read as prose."""
    return CODE_SPAN.sub(" ", text)


def unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def code_spans(text: str) -> list[str]:
    return unique(CODE_SPAN.findall(text))


def rule_citations(text: str) -> list[str]:
    return unique(RULE_CITATION.findall(text))


def plugin_paths(text: str) -> list[str]:
    return unique(PLUGIN_PATH.findall(text))


def number_value(token: str) -> str:
    return NUMBER_WORDS.get(token.lower(), token.replace(",", ""))


def numbers(text: str) -> list[str]:
    """Each number in the prose as digits, so "five" and "5" are the same item."""
    return unique([number_value(token) for token in NUMBER.findall(prose(text))])


def quoted_strings(text: str) -> list[str]:
    """Each double-quoted string in the prose, with curly quotes made straight."""
    return unique([f'"{straight or curly}"' for straight, curly in QUOTED.findall(prose(text))])


def bold_spans(text: str) -> list[str]:
    return unique(BOLD.findall(prose(text)))


def step_references(text: str) -> list[str]:
    return unique([" ".join(found.lower().split()) for found in STEP_REFERENCE.findall(prose(text))])


def headings(text: str) -> list[str]:
    return [line.rstrip() for line in text.splitlines() if line.startswith("#")]


KINDS = (
    Kind("code span", code_spans),
    Kind("rule citation", rule_citations),
    Kind("plugin path", plugin_paths),
    Kind("number", numbers),
    Kind("quoted string", quoted_strings),
    Kind("bold span", bold_spans),
    Kind("step reference", step_references),
)


def kind_differences(kind: Kind, old: str, new: str) -> list[Difference]:
    old_items = kind.items(old)
    new_items = kind.items(new)
    lost = [Difference(kind.name, item, True) for item in old_items if item not in new_items]
    added = [Difference(kind.name, item, False) for item in new_items if item not in old_items]
    return lost + added


def limiting_word_count(text: str) -> int:
    return len(LIMITING_WORD.findall(prose(text)))


def warnings(old: str, new: str) -> list[str]:
    """The changes that may shift the meaning but do not fail: fewer limiting words, and more than 10 percent growth."""
    found: list[str] = []
    old_limits, new_limits = limiting_word_count(old), limiting_word_count(new)
    if new_limits < old_limits:
        words = ", ".join(LIMITING_WORDS)
        found.append(f"warning: the words {words} went from {old_limits} to {new_limits}")
    old_words, new_words = len(old.split()), len(new.split())
    if new_words > old_words * (1 + GROWTH_CAP):
        found.append(f"warning: {old_words} words grew to {new_words}, over {GROWTH_CAP:.0%}")
    return found


def compare(old: str, new: str) -> Report:
    return Report(
        differences=tuple(difference for kind in KINDS for difference in kind_differences(kind, old, new)),
        headings_changed=headings(old) != headings(new),
        warnings=tuple(warnings(old, new)),
    )


def report_lines(page: str, report: Report) -> list[str]:
    changes = [
        f"{page}: {'lost' if difference.lost else 'added'} {difference.kind}: {difference.item}"
        for difference in report.differences
    ]
    headings_line = [f"{page}: headings changed"] if report.headings_changed else []
    return changes + headings_line + [f"{page}: {warning}" for warning in report.warnings]


def is_commit(base: str) -> bool:
    found = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}"],
        capture_output=True,
        text=True,
    )
    return found.returncode == 0


def base_text(base: str, page: str) -> str | None:
    """The page's text at the base commit, or None when the page is not there."""
    relative = Path(os.path.relpath(page)).as_posix()
    shown = subprocess.run(
        ["git", "show", f"{base}:./{relative}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return shown.stdout if shown.returncode == 0 else None


def main(arguments: list[str]) -> int:
    if len(arguments) < 2:
        print("usage: same-meaning.py <base-commit> <page>...", file=sys.stderr)
        return 2
    base, pages = arguments[0], arguments[1:]
    if not is_commit(base):
        print(f"{base}: not a commit", file=sys.stderr)
        return 2
    failed = False
    for page in pages:
        old = base_text(base, page)
        if old is None:
            print(f"{page}: new page")
            continue
        try:
            new = Path(page).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"{page}: missing from the working copy")
            failed = True
            continue
        report = compare(old, new)
        for line in report_lines(page, report):
            print(line)
        failed = failed or report.lost_something
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
