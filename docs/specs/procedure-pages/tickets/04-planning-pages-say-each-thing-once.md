**Status.** done

**What to build.** `procedures/grill.md`, `procedures/research.md`, `procedures/spec.md` and `procedures/tickets.md`: one opening line each on what it makes and for whom, keeping where it came from; no `## Subagents` section; no line saying which playbook runs it. Research drops the lines the mode's Subagents section and `references/plan-file.md` already say, and its reply becomes a short list in the same order.

**Checks.** `make check` passes before and after. `claude plugin eval . --case feature-grills-first --ablation none` passes after.

**Blocked by.** none
