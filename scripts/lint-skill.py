#!/usr/bin/env python3
"""Mechanical checks for a Claude skill folder.

Usage: python3 lint-skill.py <skill-folder-or-SKILL.md>

Prints one line per issue as `LEVEL  location  message`. Exits 0 after linting, 1 if SKILL.md is
not found, 2 on bad usage. The checks are leads for a human or model reviewer, not a verdict:
they do not judge whether the instructions are good. Uses only the standard library.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_MAX = 64
DESCRIPTION_MAX = 1024
BODY_LINES_SOFT_MAX = 500
REFERENCE_TOC_THRESHOLD = 100
SHOUT_THRESHOLD = 5
RESERVED_NAME_WORDS = ("anthropic", "claude")
SHOUT_WORDS = re.compile(r"\b(MUST|NEVER|ALWAYS|CRITICAL|IMPORTANT|REQUIRED|DO NOT)\b")
BACKSLASH_PATH = re.compile(r"\b(?:scripts|references|assets)\\[\w.\\-]+")
FENCE = re.compile(r"```.*?```", re.S)
USE_WHEN = re.compile(r"\buse\b[^.]{0,40}?\b(when|whenever|if|for)\b|\bwhen (the )?user\b|\btrigger|\bfire\b|\binvoke", re.I)
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)|`((?:references|scripts|assets)/[^`\s]+)`")
BARE_PATH = re.compile(r"(?<![\w/.$}-])((?:references|scripts|assets)/[\w./-]*\w\.\w+)")
PLUGIN_ROOT_PATH = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]*\w)")


def split_frontmatter(text: str) -> tuple[dict[str, str], list[str], str, int]:
    """Split SKILL.md into frontmatter fields, YAML problems, the body, and the body's first line.

    Args:
        text: full SKILL.md contents.

    Returns:
        (fields, yaml_issues, body, body_start_line). fields maps top-level keys to their raw
        string value, with folded/literal block scalars joined into one line; it is empty when
        there is no `---` block. yaml_issues lists plain values that YAML would reject (an
        unquoted ": " inside the value). body starts on the line after the closing `---`, and
        body_start_line is its 1-based line number in the file.
    """
    if not text.startswith("---"):
        return {}, [], text, 1
    end = text.find("\n---", 3)
    if end == -1:
        return {}, [], text, 1
    block = text[3:end].strip("\n")
    fields: dict[str, str] = {}
    yaml_issues: list[str] = []
    key = None
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            if value and value[0] not in "\"'|>" and ": " in value:
                yaml_issues.append(f"HIGH   {key}  unquoted ': ' inside the value is invalid YAML; quote it or use a '>' block")
            fields[key] = "" if value in ("|", ">", "|-", ">-") else value.strip("\"'")
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    closing_line_end = text.find("\n", end + 1)
    if closing_line_end == -1:
        return fields, yaml_issues, "", text.count("\n") + 2
    body_start = text[: closing_line_end + 1].count("\n") + 1
    return fields, yaml_issues, text[closing_line_end + 1 :], body_start


def check_frontmatter(fields: dict[str, str]) -> list[str]:
    """Return issues with `name` and `description`, per Anthropic's published limits."""
    issues: list[str] = []
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not fields:
        return ["HIGH   frontmatter  missing YAML frontmatter (--- block with name and description)"]
    if not name:
        issues.append("HIGH   name  missing")
    else:
        if len(name) > NAME_MAX:
            issues.append(f"HIGH   name  {len(name)} chars, limit {NAME_MAX}")
        if not re.fullmatch(r"[a-z0-9-]+", name):
            issues.append("HIGH   name  use lowercase letters, digits and hyphens only")
        for word in RESERVED_NAME_WORDS:
            if word in name.lower():
                issues.append(f"HIGH   name  contains reserved word '{word}'")
    if not description:
        issues.append("HIGH   description  missing or empty")
    else:
        if len(description) > DESCRIPTION_MAX:
            issues.append(f"HIGH   description  {len(description)} chars, limit {DESCRIPTION_MAX}")
        if re.search(r"<[^>]+>", description):
            issues.append("HIGH   description  contains XML/HTML tags")
        if not USE_WHEN.search(description):
            issues.append("MEDIUM description  no 'use when...' clause found; it may not say when to trigger")
        if re.match(r"\s*(I |I'm |You can )", description):
            issues.append("MEDIUM description  first/second person; write it in the third person or imperative")
    return issues


def check_body(body: str, body_start: int) -> list[str]:
    """Return issues with SKILL.md body length and emphasis density."""
    issues: list[str] = []
    lines = body.splitlines()
    if len(lines) > BODY_LINES_SOFT_MAX:
        issues.append(f"MEDIUM SKILL.md  body is {len(lines)} lines; aim for under {BODY_LINES_SOFT_MAX}")
    shouts = [
        (body_start + i, m.group(0)) for i, line in enumerate(lines) for m in SHOUT_WORDS.finditer(line)
    ]
    if len(shouts) >= SHOUT_THRESHOLD:
        where = ", ".join(f"{n}:{w}" for n, w in shouts[:8])
        issues.append(f"LOW    SKILL.md  {len(shouts)} all-caps emphasis words ({where}...); explain why instead")
    return issues


def find_links(text: str, include_code_spans: bool = True) -> set[str]:
    """Return relative file paths linked or named in markdown text, excluding URLs and fenced code.

    Fenced blocks are skipped because they usually hold example output or templates, not links
    to the skill's own files.

    Args:
        text: markdown to scan.
        include_code_spans: also count `references/...`-style paths in backticks. SKILL.md often
            names its files that way; reference files use backticks for examples, so pass False
            when scanning them for nested links.
    """
    paths = set()
    if include_code_spans:
        paths.update(BARE_PATH.findall(FENCE.sub("", text)))
    for match in LINK.finditer(FENCE.sub("", text)):
        target = match.group(1) or (match.group(2) if include_code_spans else None)
        if target and "://" not in target and not target.startswith("mailto:"):
            paths.add(target)
    return paths


def find_plugin_root(root: Path) -> Path | None:
    """Return the nearest folder at or above root that holds `.claude-plugin/`, or None outside a plugin."""
    for folder in (root, *root.parents):
        if (folder / ".claude-plugin").is_dir():
            return folder
    return None


def check_files(root: Path, skill_md_text: str) -> list[str]:
    """Return issues with linked files: missing, nested links, missing TOC, backslash paths."""
    issues: list[str] = []
    linked = find_links(skill_md_text)
    for target in sorted(set(BACKSLASH_PATH.findall(skill_md_text))):
        issues.append(f"MEDIUM SKILL.md  backslash path '{target}'; use forward slashes")
    plugin_root = find_plugin_root(root)
    for target in sorted(set(PLUGIN_ROOT_PATH.findall(skill_md_text))):
        if plugin_root is None:
            issues.append(f"LOW    SKILL.md  names '${{CLAUDE_PLUGIN_ROOT}}/{target}' outside a plugin; check it by hand")
        elif not (plugin_root / target).exists():
            issues.append(f"HIGH   SKILL.md  names '${{CLAUDE_PLUGIN_ROOT}}/{target}', which does not exist")
    for target in sorted(t for t in linked if "<" not in t):
        path = (root / target).resolve()
        if not path.exists():
            issues.append(f"HIGH   SKILL.md  links to '{target}', which does not exist")
            continue
        if path.suffix == ".md":
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            ref_links = {t for t in find_links(text, include_code_spans=False) if "<" not in t}
            for ref_target in sorted(ref_links):
                if not ((path.parent / ref_target).exists() or (root / ref_target).exists()):
                    issues.append(f"HIGH   {target}  links to '{ref_target}', which does not exist")
            nested = {t for t in ref_links if t.endswith(".md")}
            if nested:
                issues.append(f"MEDIUM {target}  links further to {sorted(nested)}; keep references one level deep")
            if text.count("\n") > REFERENCE_TOC_THRESHOLD and not re.search(r"(?im)^#+\s*(contents|table of contents)", text):
                issues.append(f"LOW    {target}  over {REFERENCE_TOC_THRESHOLD} lines with no table of contents")
    mentions = skill_md_text + "".join(
        (root / t).read_text(encoding="utf-8-sig", errors="replace")
        for t in linked if "<" not in t and t.endswith(".md") and (root / t).is_file()
    )
    if plugin_root is not None:
        mentions += "".join(
            (plugin_root / t).read_text(encoding="utf-8-sig", errors="replace")
            for t in set(PLUGIN_ROOT_PATH.findall(skill_md_text))
            if t.endswith(".md") and (plugin_root / t).is_file()
        )
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_file() and rel != "SKILL.md" and not rel.startswith(("evals/", ".")):
            named_by_slug = path.parent.name == "rules" and f"rule-{path.stem}" in skill_md_text
            if rel not in linked and path.name not in mentions and not named_by_slug:
                issues.append(f"LOW    {rel}  not mentioned in SKILL.md; Claude will not know it exists")
    return issues


def main(argv: list[str]) -> int:
    """Lint the skill named on the command line and print the issues found."""
    if len(argv) != 2:
        print(__doc__)
        return 2
    target = Path(argv[1]).expanduser()
    skill_md = target if target.name == "SKILL.md" else target / "SKILL.md"
    if not skill_md.is_file():
        print(f"HIGH   {skill_md}  not found")
        return 1
    text = skill_md.read_text(encoding="utf-8-sig", errors="replace")
    fields, yaml_issues, body, body_start = split_frontmatter(text)
    issues = yaml_issues + check_frontmatter(fields) + check_body(body, body_start) + check_files(skill_md.parent, text)
    name = fields.get("name", "")
    if name and name != skill_md.parent.name:
        issues.append(f"MEDIUM name  '{name}' does not match the folder name '{skill_md.parent.name}'")
    print(f"# {skill_md}  ({len(body.splitlines())} body lines, description {len(fields.get('description', ''))} chars)")
    print("\n".join(issues) if issues else "no mechanical issues found")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
