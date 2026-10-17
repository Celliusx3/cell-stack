**Status.** open

**What to build.** `git mv rules/split-on-the-seam.md rules/one-job-per-file.md` and retitle it. Its "data" and "decision" halves are reworded to match **rule-keep-logic-pure**, where the decision never talks to the outside. "Seam" leaves `rules/typed-boundaries.md` and its index line. Update `SKILL.md` and both language pages.

**Checks.** `make check` passes before and after. `grep -rn seam skills` finds only the reply rule that bans the word. Break: leave the old slug in one language page; lint fails.

**Blocked by.** none
