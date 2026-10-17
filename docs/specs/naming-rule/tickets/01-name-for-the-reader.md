**Status.** done

**What to build.** Replace `rules/name-what-it-returns.md` with `rules/name-for-the-reader.md`: one rule for folders, files, classes, functions and tests. A bare verb only where the receiver or module names the object; a past participle only for a returned value. Update the index line in `SKILL.md`, the rows in `languages/python.md` and `languages/typescript.md`, the citation in `playbooks/refactor.md`, and the cross-reference in `rules/group-by-subject.md`.

**Checks.** A new eval case `evals/name-a-new-function/`: on the shared ledger fixture, Claude pulls the report out of `cli.py` into one new function in `ledger.py`. It passes when Claude reads `rules/name-for-the-reader.md`, defines no function with a bare verb or noun that fits anything, and names the rule in its reply. Run with `claude plugin eval . --case name-a-new-function --ablation none`. Fails before this ticket (the page does not exist), passes after. `make check` passes.

**Blocked by.** none
