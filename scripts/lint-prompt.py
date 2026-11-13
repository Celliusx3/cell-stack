#!/usr/bin/env python3
"""Mechanical checks for a system prompt.

Usage: python3 lint-prompt.py <prompt-text-file | ->

Reads the assembled prompt text (not the source code that builds it) from a file, or from stdin
when the path is `-`. Prints one line per lead as `LEVEL  location  message`. Exits 0 after
linting, 1 if the file is missing, 2 on bad usage; errors go to stderr. The checks are leads for
a reviewer, not a verdict: they do not judge whether the instructions are good. Uses only the
standard library.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

CHARS_PER_TOKEN = 4
LARGE_PROMPT_TOKENS = 8000
SHOUT_THRESHOLD = 3
NEGATIVE_RATIO_THRESHOLD = 0.5
CACHE_PREFIX_MAX_LINES = 15
CACHE_PREFIX_FRACTION = 0.2
MIN_REPEATED_LINE_CHARS = 40
SHOUT_WORDS = re.compile(r"\b(MUST|NEVER|ALWAYS|CRITICAL|IMPORTANT|REQUIRED|REFUSE|ONLY|DO NOT|DON'T|YOU WILL|NO EXCEPTIONS)\b")
NEGATIVE = re.compile(r"\b(don't|do not|never|avoid|must not|should not|shouldn't|no )\b", re.I)
POSITIVE = re.compile(r"^\s*(?:[-*\d.]+\s*)?(use|write|answer|respond|keep|include|start|ask|say|return|prefer|cite|call|read|give|tell|explain|summari[sz]e|format|list|check|reply|show|put|choose|pick|set|treat|follow)\b", re.I)
DYNAMIC = re.compile(r"\{\{?\s*[\w.]+\s*\}?\}|\$\{[\w.]+\}|\bnow\(\)|\b(current date|timestamp|request_id|user_name)\b", re.I)
TAG = re.compile(r"<(/?)([A-Za-z_][\w-]*)(?:\s[^<>]*)?>")
FENCED_FILE = re.compile(r"\A\s*```[^\n]*\n(.*?)\n```\s*\Z", re.S)
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
VOID_LIKE = {"br", "hr", "img"}


def check_size(text: str) -> list[str]:
    """Return an INFO line with the estimated token count, and a lead when it is large."""
    tokens = len(text) // CHARS_PER_TOKEN
    out = [f"INFO   prompt  ~{tokens} tokens, {len(text.splitlines())} lines"]
    if tokens > LARGE_PROMPT_TOKENS:
        out.append(f"MEDIUM prompt  over ~{LARGE_PROMPT_TOKENS} tokens; check which sections could load on demand")
    return out


def check_emphasis(lines: list[str]) -> list[str]:
    """Return a lead when all-caps emphasis words are frequent, with their line numbers."""
    hits = [(n, m.group(0)) for n, line in enumerate(lines, 1) for m in SHOUT_WORDS.finditer(line)]
    if len(hits) < SHOUT_THRESHOLD:
        return []
    where = ", ".join(f"{n}:{w}" for n, w in hits[:10])
    return [f"MEDIUM emphasis  {len(hits)} all-caps emphasis words ({where}...); current models over-apply these"]


def check_negatives(lines: list[str]) -> list[str]:
    """Return a lead when prohibitions clearly outnumber positive instructions."""
    negatives = sum(1 for line in lines if NEGATIVE.search(line))
    positives = sum(1 for line in lines if POSITIVE.search(line))
    total = negatives + positives
    if total and negatives / total > NEGATIVE_RATIO_THRESHOLD and negatives >= 5:
        return [f"LOW    phrasing  {negatives} prohibition lines vs {positives} positive instructions; say what to do instead"]
    return []


def check_tags(text: str) -> list[str]:
    """Return leads for XML-style tags that are unbalanced.

    Code spans and fences are ignored, and so are all-caps names such as <INTERNAL_API_KEY>,
    which are placeholders. A tag that is never closed anywhere is reported at LOW, because it is
    often a placeholder or a tag named in prose ("the documents in <docs>"). A tag left open
    inside one that is later closed, or a closing tag with no opening, is reported at MEDIUM.
    """
    stack: list[str] = []
    unclosed_inside: list[str] = []
    stray: list[str] = []
    for match in TAG.finditer(CODE.sub("", text)):
        closing, raw = match.group(1) == "/", match.group(2)
        name = raw.lower()
        if raw.isupper() or name in VOID_LIKE or match.group(0).endswith("/>"):
            continue
        if not closing:
            stack.append(name)
        elif name in stack:
            while stack:
                top = stack.pop()
                if top == name:
                    break
                unclosed_inside.append(top)
        else:
            stray.append(name)
    out = []
    if unclosed_inside:
        out.append(f"MEDIUM tags  left open inside a closed tag: {sorted(set(unclosed_inside))}")
    if stray:
        out.append(f"MEDIUM tags  closed without opening: {sorted(set(stray))}")
    if stack:
        out.append(f"LOW    tags  never closed (unclosed block, or a placeholder/prose mention): {sorted(set(stack))}")
    return out


def check_cache_prefix(lines: list[str]) -> list[str]:
    """Return a lead when per-request values appear near the top, which breaks prompt caching.

    "Near the top" is the first 20% of lines, capped at 15, so a value correctly placed at the
    end of a short prompt is not flagged.
    """
    limit = min(CACHE_PREFIX_MAX_LINES, max(1, int(len(lines) * CACHE_PREFIX_FRACTION)))
    hits = [n for n, line in enumerate(lines[:limit], 1) if DYNAMIC.search(line)]
    if not hits:
        return []
    return [f"MEDIUM caching  per-request value near the top (lines {hits}); move it after the stable instructions"]


def check_repeats(lines: list[str]) -> list[str]:
    """Return a lead for long lines that appear more than once verbatim."""
    counts = Counter(line.strip() for line in lines if len(line.strip()) >= MIN_REPEATED_LINE_CHARS)
    repeated = [line for line, count in counts.items() if count > 1]
    if not repeated:
        return []
    sample = repeated[0][:60]
    return [f"LOW    repeats  {len(repeated)} line(s) repeated verbatim, e.g. '{sample}...'"]


def main(argv: list[str]) -> int:
    """Lint the prompt named on the command line and print the leads found."""
    if len(argv) != 2:
        print(__doc__)
        return 2
    if argv[1] == "-":
        text = sys.stdin.read()
    else:
        path = Path(argv[1]).expanduser()
        if not path.is_file():
            print(f"error: {path} not found", file=sys.stderr)
            return 1
        text = path.read_text(encoding="utf-8", errors="replace")
    whole_file_fence = FENCED_FILE.match(text)
    if whole_file_fence:
        text = whole_file_fence.group(1)
    lines = text.splitlines()
    leads = (
        check_size(text)
        + check_emphasis(lines)
        + check_negatives(lines)
        + check_tags(text)
        + check_cache_prefix(lines)
        + check_repeats(lines)
    )
    print("\n".join(leads))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
