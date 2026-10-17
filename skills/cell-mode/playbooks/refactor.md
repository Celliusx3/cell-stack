### Refactor

**You own what the code does. The arrangement changes; the behaviour does not.** A bug or a missing feature found on the way is named in the reply and left for its own change, never folded in.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. Read the code and every caller. List what the code promises (what it returns, saves, raises, and in what order) and which test checks each promise. Run those tests once and paste the command and the result. For a UI change the test is a rendered snapshot or a screenshot of every state, taken before and compared after; no baseline, no claim that it looks the same. Type check and lint do not count. A promise with no test is listed as the first test to write; it is not written yet.
3. Say what the change makes better: what it lets you delete (a branch, an argument threaded through, a one-call wrapper, an impossible state), or what it makes clear (a name that says what it returns, per **rule-name-what-it-returns**). A new model or class is added only where **rule-typed-boundaries** or **rule-group-by-subject** earns it. If the change only adds a layer, it is not worth doing; say so and stop.
4. Say the end state in plain words, with one example of the code after it lands, then how many files change. More than about five files: that is two refactors; do the first.

**Plan mode stops here.** Steps 1 to 4 run during planning; the plan is steps 5 to 12.

5. Write each missing test from step 2 and run it on the code as it is. It passes; paste the command and the result.
6. When the whole change is under about ten lines, make the edits in steps 7 and 8 yourself and say so in the reply. Otherwise hand them to one `general-purpose` subagent with the exact scope: the files, the names being moved, the promises that must hold, the language page for the file type.
7. Remove before you add: dead code, one-call wrappers (**rule-no-pass-through**), leftover references. Then the smallest change that reaches the end state (**rule-smallest-change**).
8. Move one thing, run the tests, move the next; whoever makes the edits runs them. Update every caller and delete the old name in the same move; never keep old and new side by side. Grep each rename against strings, docs and tests.
9. Review the diff yourself and run the tests yourself. Paste the command and the result.
10. Break it on purpose: for each moved piece, change one line so it is wrong and check that a test fails. A test that stays green was not watching; write one that does. Undo the break. Paste commands and results.
11. Easier to read? Fewer functions to keep track of, fewer branches, or one named type where loose values were passed around. Say which in one line. If none, undo the whole thing and say why.
12. Run `/strip-comments` on the diff. Write the commits in order (removal, reshape, cleanup), each with its message. Make none unless asked; when asked, run `/commit`.

**Reply:** what reads easier, first, and that nothing the person sees changes; what moved and what was deleted; the tests that guarded it and the proof (commands and results, including the break-on-purpose); what was undone; the commits proposed.
