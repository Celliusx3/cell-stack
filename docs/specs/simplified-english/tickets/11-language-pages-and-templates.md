**Status.** done

**What to build.** Rewrite `languages/python.md`, `languages/typescript.md`, `templates/rule.md`, `procedures/write-how-to-use/example-feature-map/README.md` and `procedures/write-how-to-use/example-feature-map/search.md` in the Writing style. The script counts the sentences in table cells too. Add the five pages to the lint list.

**Checks.** `scripts/long-sentences.py` passes on each page, table cells included. `scripts/same-meaning.py 2409dbd` reports no loss on each page. `make check` passes.

**Blocked by.** 02
