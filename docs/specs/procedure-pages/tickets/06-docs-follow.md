**Status.** done

**What to build.** `README.md`: the page table (write-how-to-use, no Verify step) and the hook line. `docs/adding-a-skill.md`: a procedure is wired by its line in the mode's Procedures list; what a procedure page holds (one opening line, Steps, Reply, no Subagents section); the naming line points at **rule-name-for-the-reader**; the lint table gains the two new checks.

**Checks.** `make check` passes. A search of `README.md` and `docs/adding-a-skill.md` for a slash command other than `/cell-mode`, the old drive page, or a Verify step finds nothing.

**Blocked by.** 01, 02, 03, 04, 05
