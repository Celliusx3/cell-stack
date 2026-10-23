**Status.** done

**What to build.** Rewrite `procedures/grill.md`, `procedures/spec.md`, `procedures/tickets.md`, `procedures/commit.md` and `procedures/research.md` in the Writing style. Each page that makes a text for a person points at the Writing section. Those texts are the questions, the spec, the tickets, the commit message, and the research reply. Add the five pages to the lint list.

**Checks.** `scripts/long-sentences.py` fails on each page before and passes after. `scripts/same-meaning.py 2409dbd` reports no loss on each page. `make check` passes.

**Blocked by.** 02
