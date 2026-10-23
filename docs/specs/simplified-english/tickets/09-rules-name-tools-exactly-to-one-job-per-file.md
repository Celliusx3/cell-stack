**Status.** open

**What to build.** Rewrite `rules/name-tools-exactly.md`, `rules/no-name-switch.md`, `rules/no-pass-through.md`, `rules/one-id-one-meaning.md`, `rules/one-job-per-file.md` in the Writing style. Each rule keeps its title line, its When, its Rule and its test, with the same meaning. Add the five pages to the lint list.

**Checks.** `scripts/long-sentences.py` passes on each page. `scripts/same-meaning.py 2409dbd` reports no loss on each page. `make check` passes.

**Blocked by.** 02
