#!/usr/bin/env bash
# After an Edit or Write to a .md file under a plans or specs folder, tell the model to split each sentence over the Writing caps.
set -euo pipefail
file=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path") or "")') || exit 0
case "$file" in
	*/plans/*.md|*/specs/*.md|plans/*.md|specs/*.md) ;;
	*) exit 0 ;;
esac
[ -f "$file" ] || exit 0
root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
findings=$(python3 "$root/scripts/long-sentences.py" "$file" || true)
[ -n "$findings" ] || exit 0
python3 - "$file" "$findings" <<'PY' || true
import json, sys
path, printed = sys.argv[1], sys.argv[2].splitlines()
count = len(printed)
subject = f"1 sentence in {path} is" if count == 1 else f"{count} sentences in {path} are"
label = "The first three findings:" if count > 3 else "Findings:"
context = "\n".join([
    f"{subject} over the Writing caps. Split each one as the Writing section of cell mode says, before you hand back.",
    label,
    *printed[:3],
])
print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": context}}))
PY
exit 0
