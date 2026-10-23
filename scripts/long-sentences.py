#!/usr/bin/env python3
"""Prints each sentence in the given Markdown files that is over the Writing caps, and exits 1 when there is one."""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

STEP_CAP = 20
SENTENCE_CAP = 25
PARAGRAPH_CAP = 6

NUMBERED_ITEM = re.compile(r"^(\s*)\d+\.\s+")
BULLET_ITEM = re.compile(r"^(\s*)[-*]\s+")
FENCE = re.compile(r"^\s*(```|~~~)")
TABLE_SEPARATOR = re.compile(r"^\s*\|?(\s*:?-+:?\s*\|)+\s*:?-*:?\s*\|?\s*$")
CODE_SPAN = re.compile(r"`[^`]*`")
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
SENTENCE_END = re.compile(r"(?<=[.?!])[\"'”’)\]*_]*\s+")


@dataclass(frozen=True)
class Block:
    line: int
    text: str
    cap: int


@dataclass(frozen=True)
class Finding:
    line: int
    message: str


def body_lines(text: str) -> list[tuple[int, str]]:
    """The numbered lines a reader sees as prose: no frontmatter, fenced code or headings."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        closing = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), 0)
        start = closing + 1
    kept: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(lines[start:], start + 1):
        if FENCE.match(line):
            in_fence = not in_fence
            kept.append((number, ""))
        elif in_fence or line.lstrip().startswith("#"):
            kept.append((number, ""))
        else:
            kept.append((number, line))
    return kept


def table_cells(number: int, row: str) -> list[Block]:
    cells = row.replace("\\|", "¦").strip().strip("|").split("|")
    return [Block(number, cell.strip(), SENTENCE_CAP) for cell in cells if cell.strip()]


def blocks(text: str) -> list[Block]:
    """Each paragraph, list item and table cell, with the cap its sentences must keep."""
    lines = body_lines(text)
    found: list[Block] = []
    current: Block | None = None
    for index, (number, line) in enumerate(lines):
        next_line = lines[index + 1][1] if index + 1 < len(lines) else ""
        if not line.strip():
            current = None
        elif line.lstrip().startswith("|"):
            current = None
            if not TABLE_SEPARATOR.match(line) and not TABLE_SEPARATOR.match(next_line):
                found.extend(table_cells(number, line))
        elif NUMBERED_ITEM.match(line) or BULLET_ITEM.match(line):
            cap = STEP_CAP if NUMBERED_ITEM.match(line) else SENTENCE_CAP
            marker = NUMBERED_ITEM.match(line) or BULLET_ITEM.match(line)
            current = Block(number, line[marker.end():], cap)
            found.append(current)
        elif current is not None:
            current = Block(current.line, f"{current.text} {line.strip().lstrip('>')}", current.cap)
            found[-1] = current
        else:
            current = Block(number, line.strip().lstrip(">"), SENTENCE_CAP)
            found.append(current)
    return found


def sentences(text: str) -> list[str]:
    plain = LINK.sub(r"\1", CODE_SPAN.sub("CODE", text))
    return [part for part in SENTENCE_END.split(plain.strip()) if part.strip()]


def word_count(sentence: str) -> int:
    return sum(1 for token in sentence.split() if any(char.isalnum() for char in token))


def findings(block: Block) -> list[Finding]:
    parts = sentences(block.text)
    over = [
        Finding(block.line, f"{word_count(part)} words, cap {block.cap}: {' '.join(part.split()[:8])} ...")
        for part in parts
        if word_count(part) > block.cap
    ]
    if len(parts) > PARAGRAPH_CAP:
        over.append(Finding(block.line, f"{len(parts)} sentences in one paragraph, cap {PARAGRAPH_CAP}"))
    return over


def long_sentences(text: str) -> list[Finding]:
    return [finding for block in blocks(text) for finding in findings(block)]


def main(paths: list[str]) -> int:
    count = 0
    for path in paths:
        for finding in long_sentences(Path(path).read_text()):
            print(f"{path}:{finding.line}: {finding.message}")
            count += 1
    return 1 if count else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
