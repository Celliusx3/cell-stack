#!/usr/bin/env bash
# Adds a rule: copies templates/rule.md to skills/cell-mode/rules/<slug>.md, appends its line to cell-mode's rules list, and runs lint.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
name="${1:-}"
[[ "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "name must be kebab-case" >&2; exit 2; }
slug="${name#rule-}"
mode="skills/cell-mode/SKILL.md"
dst="skills/cell-mode/rules/$slug.md"
[ -e "$dst" ] && { echo "$dst exists" >&2; exit 1; }
sed "s/NAME/rule-$slug/" templates/rule.md > "$dst"
printf -- '- **rule-%s**. When it applies, in one line. The rule, in one line.\n' "$slug" >> "$mode"
echo "created $dst and an index line at the end of $mode (move it under ## Rules)"
scripts/lint.sh
