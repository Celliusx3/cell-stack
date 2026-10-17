**Status.** open

**What to build.** Take the naming sentences out of `rules/place-by-kind.md` and `rules/group-by-subject.md`; each points at **rule-name-for-the-reader** instead. Their index lines in `SKILL.md` and rows in both language pages follow. `languages/typescript.md` drops its "more than two arguments" line and the two lines that repeat its typed-boundaries row. `languages/python.md` moves its test-naming line into the naming rule's row.

**Checks.** `make check` passes before and after. `claude plugin eval . --case refactor-adds-a-sibling --ablation none` passes after. Break: remove the naming rule's index line; lint fails.

**Blocked by.** 01
