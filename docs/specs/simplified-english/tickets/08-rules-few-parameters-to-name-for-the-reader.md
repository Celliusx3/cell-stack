**Status.** done

**What to build.** Rewrite `rules/few-parameters.md`, `rules/group-by-subject.md`, `rules/keep-logic-pure.md`, `rules/leave-generated-alone.md`, `rules/name-for-the-reader.md` in the Writing style. Each rule keeps its title line, its When, its Rule and its test, with the same meaning. Add the five pages to the lint list.

**Checks.** `scripts/long-sentences.py` passes on each page. `scripts/same-meaning.py 2409dbd` reports no loss on each page. `make check` passes.

**Blocked by.** 02
