**Status.** open

**What to build.** `procedures/commit.md`, `procedures/strip-comments.md` and `procedures/write-how-to-use.md` get the same cuts as ticket 04. Strip comments moves `## Scope` into step 1 and drops the pstack notes. Commit's step 1 records the starting commit as the base that step 6 resets to. Write-how-to-use's step 3 points at the example for a feature file's shape instead of repeating it, and step 4 says the agent that wrote the skill runs it.

**Checks.** `make check` passes before and after. `claude plugin eval . --case strip-comments --ablation none` and `--case commit-finds-its-page` pass after.

**Blocked by.** 03
