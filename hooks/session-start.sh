#!/usr/bin/env bash
# At session start, put cell mode into context so plain requests route to a
# playbook without anyone typing /cell-mode. The body is the skill file itself.
set -euo pipefail
root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
python3 - "$root" <<'PY'
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
text = (root / "skills/cell-mode/SKILL.md").read_text()
body = text.split("---", 2)[2].strip() if text.startswith("---") else text
body = body.replace("${CLAUDE_PLUGIN_ROOT}", str(root))
context = "Cell mode is on for this session (cellstack). Apply it as written:\n\n" + body
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}))
PY
