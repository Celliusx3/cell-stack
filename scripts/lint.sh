#!/usr/bin/env bash
# The structure rules. Exit 1 naming the file and the rule it broke, so a new
# page that does not fit the shape is refused before it is ever typed.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root" || exit 1
mode="skills/cell-mode/SKILL.md"
fail=0
bad() { printf '%s: %s\n' "$1" "$2" >&2; fail=1; }

for d in skills/*/; do
	[ -d "$d" ] || continue
	[ "$d" = "skills/cell-mode/" ] || bad "$d" "only cell-mode is a skill; other pages live inside it"
done
if [ -f "$mode" ]; then
	fm=$(awk 'NR==1 && $0!="---"{exit} NR>1 && $0=="---"{exit} NR>1{print}' "$mode")
	keys=$(printf '%s\n' "$fm" | grep -oE '^[a-z-]+:' | tr -d ':' | sort | tr '\n' ' ')
	[ "$keys" = "description disable-model-invocation name " ] || bad "$mode" "frontmatter must be exactly name, description, disable-model-invocation (got: ${keys:-none})"
	printf '%s\n' "$fm" | grep -q '^disable-model-invocation: true$' || bad "$mode" "disable-model-invocation must be true"
	name=$(printf '%s\n' "$fm" | sed -n 's/^name: //p')
	[ "$name" = "cell-mode" ] || bad "$mode" "name '$name' must be cell-mode"
fi
while read -r f; do
	[ "$f" = "$mode" ] && continue
	[ "$(head -1 "$f")" != "---" ] || bad "$f" "a page has no frontmatter; only cell-mode/SKILL.md is a skill"
done < <(find skills/cell-mode -type f -name '*.md' | sort)

if [ -f "$mode" ]; then
	# 2. every playbook has a routing row, and every row points at a file
	for p in skills/cell-mode/playbooks/*.md; do
		[ -f "$p" ] || continue
		grep -q "\`playbooks/$(basename "$p")\`" "$mode" || bad "$p" "no routing row in $mode"
	done
	while read -r ref; do
		[ -f "skills/cell-mode/$ref" ] || bad "$mode" "routing row points at missing $ref"
	done < <(grep -oE '`playbooks/[a-z0-9-]+\.md`' "$mode" | tr -d '`' | sort -u)
	for p in skills/cell-mode/procedures/*.md; do
		[ -f "$p" ] || continue
		grep -qE "^- \*\*[^*]+\*\* \(\`[^\`]*/procedures/$(basename "$p")\`\)" "$mode" || bad "$p" "not in the procedures list of $mode"
	done
	# 3. every rule is in the index, and every rule a page cites has its page
	for r in skills/cell-mode/rules/*.md; do
		[ -f "$r" ] || continue
		slug="rule-$(basename "$r" .md)"
		grep -q "\*\*$slug\*\*" "$mode" || bad "$r" "not in the rules index of $mode (expected **$slug**)"
	done
	while IFS=: read -r f slug; do
		slug="${slug//\*/}"
		[ -f "skills/cell-mode/rules/${slug#rule-}.md" ] || bad "$f" "cites **$slug** but rules/${slug#rule-}.md is missing"
	done < <(grep -roE '\*\*rule-[a-z0-9-]+\*\*' skills | sort -u)
fi

plugin_root_prefix='${CLAUDE_PLUGIN_ROOT}/'
while IFS=: read -r f ref; do
	path="${ref#"$plugin_root_prefix"}"
	[ -e "$path" ] || bad "$f" "points at missing $path"
done < <(grep -roE '\$\{CLAUDE_PLUGIN_ROOT\}/[A-Za-z0-9_./-]+' skills)

# 3b. a language page spells every rule in the index
if [ -f "$mode" ]; then
	for f in skills/cell-mode/languages/*.md; do
		[ -f "$f" ] || continue
		for slug in $(grep -oE '\*\*rule-[a-z0-9-]+\*\*' "$mode" | tr -d '*' | sort -u); do
			grep -q "\*\*$slug\*\*" "$f" || bad "$f" "does not say how $slug is spelled"
		done
	done
fi

# 4. a procedure that spawns carries its prompt
for f in skills/cell-mode/procedures/*.md; do
	[ -f "$f" ] || continue
	if grep -qi '\bspawn' "$f"; then
		ls "${f%.md}"/*.md >/dev/null 2>&1 || bad "$f" "says spawn but has no prompt in procedures/$(basename "$f" .md)/"
	fi
done

while IFS=: read -r f cmd; do
	[ "$cmd" = '`/cell-mode`' ] || bad "$f" "names $cmd, which is not a command; name the page by its path"
done < <(grep -roE '`/[a-z][a-z-]*`' skills hooks | sort -u)

# 5. word caps, and 5 to 15 steps in a playbook
words_without_list_markers() { sed -E 's/^[[:space:]]*([0-9]+\.|[-*])[[:space:]]+//' "$1" | wc -w | tr -d ' '; }
for p in skills/cell-mode/playbooks/*.md; do
	[ -f "$p" ] || continue
	n=$(words_without_list_markers "$p"); [ "$n" -le 950 ] || bad "$p" "$n words, cap is 950"
	s=$(grep -cE '^[0-9]+\.' "$p"); { [ "$s" -ge 5 ] && [ "$s" -le 15 ]; } || bad "$p" "$s numbered steps, a playbook has 5 to 15"
done
if [ -f "$mode" ]; then
	n=$(words_without_list_markers "$mode"); [ "$n" -le 2700 ] || bad "$mode" "$n words, cap is 2700"
fi
while read -r f; do
	n=$(words_without_list_markers "$f"); [ "$n" -le 1100 ] || bad "$f" "$n words, cap is 1100"
done < <(find skills/cell-mode -type f -name '*.md' ! -path "$mode" ! -path 'skills/cell-mode/playbooks/*' | sort)

# 6. playbook steps are in a new hire's words, not pstack's
for p in skills/cell-mode/playbooks/*.md; do
	[ -f "$p" ] || continue
	hit=$(grep -n -i -E '\bpin(s|ned|ning)?\b|characteri[sz]ation test|\bmutation\b|reader load|\bsubtract' "$p" | head -1 || true)
	[ -z "$hit" ] || bad "$p" "pstack word, say it plainly: $hit"
done

# 7. nothing in a page is project-specific
while read -r h; do bad "$h" "names a project; pages are generic"; done < <(grep -rln -i -E 'cell-harness|cellstudio|compaction' skills templates 2>/dev/null)

# 8. no em dash anywhere
while read -r h; do bad "$h" "contains an em dash"; done < <(grep -rln '—' --include='*.md' skills templates docs README.md 2>/dev/null)

# 9. every page keeps the Writing caps of the mode
pages=()
while read -r f; do pages+=("$f"); done < <(find skills templates -type f -name '*.md' | sort)
pages+=(docs/adding-a-skill.md README.md)
if ! out=$(python3 scripts/long-sentences.py "${pages[@]}" 2>&1); then
	printf '%s\n' "$out" >&2
	fail=1
fi

# 10. the checker still catches a long step and a long sentence
sample=$(mktemp)
printf '1. %s\n\n%s\n' "$(printf 'one %.0s' {1..21})" "$(printf 'two %.0s' {1..26})" > "$sample"
[ "$(python3 scripts/long-sentences.py "$sample" | wc -l | tr -d ' ')" -eq 2 ] || bad scripts/long-sentences.py "no longer catches a 21-word step and a 26-word sentence, the Writing caps of 20 and 25 in skills/cell-mode/SKILL.md"
rm -f "$sample"

[ "$fail" -eq 0 ] && echo "lint: clean"
exit "$fail"
