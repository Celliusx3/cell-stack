**Status.** done

**What to build.** `git mv rules/spell-the-call.md rules/name-tools-exactly.md` and retitle it. Update `SKILL.md`, both language pages, and the citations in `playbooks/fix.md` and `playbooks/build.md`.

**Checks.** `make check` passes before and after. `grep -rn spell-the-call skills docs evals README.md` finds nothing outside eval results. Break: leave the old slug in a playbook; it is caught by the grep.

**Blocked by.** none
