#!/usr/bin/env bash
# The one way to add a skill. Copies the kind's template, fills the name, adds
# the wiring line the kind needs, and runs lint so a wrong shape is refused now.
# Usage: scripts/new-skill.sh <steering|procedure|playbook|rule|language> <name>
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
kind="${1:-}"; name="${2:-}"
[[ "$kind" =~ ^(steering|procedure|playbook|rule|language)$ ]] || { echo "kind must be steering, procedure, playbook, rule or language" >&2; exit 2; }
[[ "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "name must be kebab-case" >&2; exit 2; }
mode="skills/cell-mode/SKILL.md"
title="$(printf '%s' "$name" | sed 's/-/ /g' | awk '{ $1 = toupper(substr($1,1,1)) substr($1,2) } 1')"

case "$kind" in
	playbook)
		dst="skills/cell-mode/playbooks/$name.md"
		[ -e "$dst" ] && { echo "$dst exists" >&2; exit 1; }
		[ -f "$mode" ] || { echo "$mode does not exist yet; build the mode first" >&2; exit 1; }
		sed "s/NAME/$title/" templates/playbook.md > "$dst"
		# the routing row, appended under the Playbooks heading
		printf -- '- **%s.** When it matches. `playbooks/%s.md`\n' "$title" "$name" >> "$mode"
		echo "created $dst and a routing row at the end of $mode (move it under ## Playbooks)"
		;;
	rule)
		[[ "$name" == rule-* ]] || name="rule-$name"
		dst="skills/$name/SKILL.md"
		[ -e "$dst" ] && { echo "$dst exists" >&2; exit 1; }
		[ -f "$mode" ] || { echo "$mode does not exist yet; build the mode first" >&2; exit 1; }
		mkdir -p "skills/$name"
		sed "s/NAME/$name/" templates/rule.md > "$dst"
		printf -- '- **%s**. When it applies, in one line. The rule, in one line.\n' "$name" >> "$mode"
		echo "created $dst and an index line at the end of $mode (move it under ## Rules)"
		;;
	steering|procedure|language)
		dst="skills/$name/SKILL.md"
		[ -e "$dst" ] && { echo "$dst exists" >&2; exit 1; }
		mkdir -p "skills/$name"
		sed "s/NAME/$name/" "templates/$kind.md" > "$dst"
		[ "$kind" = procedure ] && mkdir -p "skills/$name/references"
		[ "$kind" = language ] && { mkdir -p "skills/$name/references"; printf "# %s patterns\n\nOne before / after per rule.\n" "$name" > "skills/$name/references/patterns.md"; }
		echo "created $dst"
		;;
esac
scripts/lint.sh
