**Status.** done

**What to build.** Every `/commit`, `/drive`, `/strip-comments` and `/research` in `SKILL.md`, `playbooks/build.md`, `playbooks/fix.md`, `playbooks/refactor.md`, `playbooks/feature.md` and `references/plan-file.md` becomes the page's full path. The mode's pointer to the five kinds of comment that may stay names `procedures/strip-comments/reviewer-prompt.md`. The message in `hooks/comment-nag.sh` names the strip-comments page. `scripts/lint.sh` fails on a backticked slash command in a page other than `/cell-mode`.

**Checks.** `make check` passes before and after. A search of `skills/` and `hooks/` for a backticked `/commit`, `/drive`, `/strip-comments` or `/research` finds nothing. Break: write "run `/commit`" into a playbook; lint fails.

**Blocked by.** 01
