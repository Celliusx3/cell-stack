**Status.** done

**What to build.** Rewrite `playbooks/fix.md`, `playbooks/investigate.md` and `playbooks/explain.md` the same way as ticket 05. A walk through an example keeps three to six steps, with one thing happening in each step. Add the three playbooks to the lint list.

**Checks.** `scripts/long-sentences.py` passes on each playbook. `scripts/same-meaning.py 2409dbd` reports no loss on each playbook. `make check` passes. The Explain and Investigate evals pass.

**Blocked by.** 02
