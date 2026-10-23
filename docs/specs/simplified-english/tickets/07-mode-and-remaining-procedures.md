**Status.** done

**What to build.** Rewrite the rest of `SKILL.md`, `procedures/strip-comments.md`, `procedures/write-how-to-use.md`, `procedures/research/researcher-prompt.md` and `procedures/strip-comments/reviewer-prompt.md` in the Writing style. The five exceptions in the reviewer prompt keep their exact meaning. Add the five pages to the lint list.

**Checks.** `scripts/long-sentences.py` passes on each page. `scripts/same-meaning.py 2409dbd` reports no loss on each page. `make check` passes.

**Blocked by.** 05
