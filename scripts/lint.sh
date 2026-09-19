#!/usr/bin/env bash
# The structure rules. Exit 1 naming the file and the rule it broke, so a new
# skill that does not fit the shape is refused before it is ever typed.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root" || exit 1
mode="skills/cell-mode/SKILL.md"
fail=0
bad() { printf '%s: %s\n' "$1" "$2" >&2; fail=1; }

# 1. exactly three frontmatter fields, and name equals the directory
for f in skills/*/SKILL.md; do
	[ -f "$f" ] || continue
	dir=$(basename "$(dirname "$f")")
	fm=$(awk 'NR==1 && $0!="---"{exit} NR>1 && $0=="---"{exit} NR>1{print}' "$f")
	keys=$(printf '%s\n' "$fm" | grep -oE '^[a-z-]+:' | tr -d ':' | sort | tr '\n' ' ')
	[ "$keys" = "description disable-model-invocation name " ] || bad "$f" "frontmatter must be exactly name, description, disable-model-invocation (got: ${keys:-none})"
	printf '%s\n' "$fm" | grep -q '^disable-model-invocation: true$' || bad "$f" "disable-model-invocation must be true"
	name=$(printf '%s\n' "$fm" | sed -n 's/^name: //p')
	[ "$name" = "$dir" ] || bad "$f" "name '$name' must equal directory '$dir'"
	[[ "$dir" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || bad "$f" "directory must be kebab-case"
done

if [ -f "$mode" ]; then
	# 2. every playbook has a routing row, and every row points at a file
	for p in skills/cell-mode/playbooks/*.md; do
		[ -f "$p" ] || continue
		grep -q "\`playbooks/$(basename "$p")\`" "$mode" || bad "$p" "no routing row in $mode"
	done
	grep -oE '`playbooks/[a-z0-9-]+\.md`' "$mode" | tr -d '`' | sort -u | while read -r ref; do
		[ -f "skills/cell-mode/$ref" ] || bad "$mode" "routing row points at missing $ref"
	done
	# 3. every rule is in the index
	for d in skills/rule-*/; do
		[ -d "$d" ] || continue
		slug=$(basename "$d")
		grep -q "\*\*$slug\*\*" "$mode" || bad "$d" "not in the rules index of $mode (expected **$slug**)"
	done
fi

# 4. a procedure that spawns carries its prompt
for f in skills/*/SKILL.md; do
	[ -f "$f" ] || continue
	d=$(dirname "$f")
	case "$d" in skills/cell-mode|skills/rule-*) continue;; esac
	if grep -qi '\bspawn' "$f"; then
		ls "$d"/references/*.md >/dev/null 2>&1 || bad "$f" "says spawn but has no references/*-prompt.md"
	fi
done

# 5. size caps
for f in skills/*/SKILL.md; do
	[ -f "$f" ] || continue
	n=$(wc -l < "$f"); [ "$n" -le 150 ] || bad "$f" "$n lines, cap is 150"
done
for p in skills/cell-mode/playbooks/*.md; do
	[ -f "$p" ] || continue
	n=$(wc -l < "$p"); [ "$n" -le 40 ] || bad "$p" "$n lines, playbook cap is 40"
done

# 6. playbook steps are in a new hire's words, not pstack's
for p in skills/cell-mode/playbooks/*.md; do
	[ -f "$p" ] || continue
	hit=$(grep -n -i -E '\bpin(s|ned|ning)?\b|characteri[sz]ation test|\bmutation\b|reader load|\bsubtract' "$p" | head -1 || true)
	[ -z "$hit" ] || bad "$p" "pstack word, say it plainly: $hit"
done

# 7. no em dash anywhere
hits=$(grep -rln '—' --include='*.md' skills templates docs README.md 2>/dev/null)
[ -z "$hits" ] || { printf '%s\n' "$hits" | while read -r h; do bad "$h" "contains an em dash"; done; fail=1; }

[ "$fail" -eq 0 ] && echo "lint: clean"
exit "$fail"
