#!/usr/bin/env bash
# After an Edit or Write: count the comment lines the edit added and, if any,
# tell the model to run /strip-comments before handing back. The edit stands.
set -euo pipefail
file=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')
[ -n "$file" ] && [ -f "$file" ] || exit 0
case "$file" in
	*.py) pattern='^\+[[:space:]]*#' ;;
	*.ts|*.tsx) pattern='^\+[[:space:]]*(//|/\*|\*)' ;;
	*) exit 0 ;;
esac
dir=$(dirname "$file")
if git -C "$dir" rev-parse --is-inside-work-tree >/dev/null 2>&1 && git -C "$dir" ls-files --error-unmatch "$file" >/dev/null 2>&1; then
	count=$(git -C "$dir" diff -U0 -- "$file" | grep -cE "$pattern" || true)
else
	# Untracked or outside git: every comment line in the file is new.
	count=$(sed 's/^/+/' "$file" | grep -cE "$pattern" || true)
fi
[ "$count" -gt 0 ] || exit 0
name=$(basename "$file")
printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s comment lines added to %s; run /strip-comments before handing back"}}\n' "$count" "$name"
