**Status.** done

**What to build.** Rewrite `playbooks/feature.md`, `playbooks/build.md` and `playbooks/refactor.md` in the Writing style. Each keeps its numbered steps and their numbers. The one-action sub-steps go under each step as a nested numbered list. The PR text in Build points at the Writing section.

In `SKILL.md`, the playbook paragraph copies only the numbered steps into the todo list, not the sub-steps. Add the three playbooks to the lint list.

**Checks.** `scripts/long-sentences.py` passes on each playbook. The word caps and the step count in lint pass. `scripts/same-meaning.py 2409dbd` reports no loss on each playbook. `make check` passes.

**Blocked by.** 02
