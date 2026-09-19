### Refactor

**You own what the code does. The arrangement changes; the behaviour does not.** A bug or a missing feature found on the way is named in the reply and left for its own change, never folded in.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. Run the tests first. Read the code and every caller. List what the code promises (what it returns, saves, raises, and in what order) and which test checks each promise. Run those tests and paste the command and the result. A promise with no test gets one now, before anything moves. Type check and lint do not count.
3. Name what the code is missing, per **rule-group-by-subject** and **rule-typed-boundaries**: the class or model, named subject plus role, and what it lets you delete (a branch, an argument threaded through, an impossible state). If it only adds a layer, it is not worth doing; say so and stop.
4. Say the end state in three lines: which files, which types, who calls whom. More than about five files: that is two refactors; do the first.
5. Remove before you add: dead code, one-call wrappers (**rule-no-pass-through**), leftover references. Then the smallest change that reaches the end state (**rule-smallest-change**).
6. Move one thing, run the tests, move the next. Update every caller and delete the old name in the same step; never keep old and new side by side. Grep each rename against strings, docs and tests. Mechanical edits across many files may go to one `general-purpose` subagent with the exact scope; you review the diff.
7. Break it on purpose: for each moved piece, change one line so it is wrong and check that a test fails. A test that stays green was not watching; write one that does. Undo the break. Paste commands and results.
8. Easier to read? Fewer functions to relate, fewer branches, a named shape. If not, undo the whole thing and say why.
9. Run `/strip-comments` on the diff. Write the commits in order (removal, reshape, cleanup), each with its message. Make none unless asked.

**Reply:** what moved, the tests that guarded it, the proof (commands and results, including the break-on-purpose), what reads easier, what was undone, the commits proposed. No new behaviour.
