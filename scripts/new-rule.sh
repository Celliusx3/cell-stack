#!/usr/bin/env bash
# Adds a rule: copies templates/rule.md, appends its line to cell-mode's rules list, and runs lint.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
name="${1:-}"
[[ "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "name must be kebab-case" >&2; exit 2; }
[[ "$name" == rule-* ]] || name="rule-$name"
mode="skills/cell-mode/SKILL.md"
dst="skills/$name/SKILL.md"
[ -e "$dst" ] && { echo "$dst exists" >&2; exit 1; }
mkdir -p "skills/$name"
sed "s/NAME/$name/" templates/rule.md > "$dst"
printf -- '- **%s**. When it applies, in one line. The rule, in one line.\n' "$name" >> "$mode"
echo "created $dst and an index line at the end of $mode (move it under ## Rules)"
scripts/lint.sh
