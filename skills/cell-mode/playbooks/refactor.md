### Refactor

**You own what the code does. The arrangement changes, but the behaviour does not.** A bug or a missing feature found on the way is named in the reply. It is left for its own change, never mixed in.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules.
   1. If the change touches the rule files it links, open them.
2. Read the code and every caller.
   1. List what the code promises: what it returns, saves and raises, and in what order.
   2. List which test checks each promise.
   3. Run those tests once.
   4. Paste the command and the result.
   5. For a UI change, the test is a rendered snapshot or a screenshot of every state.
   6. Take the snapshot before the change.
   7. Compare it after the change. With no baseline, make no claim that it looks the same.
   8. Do not count a type check or lint as a test.
   9. List a promise with no test as the first test to write. Do not write it yet.
3. Check the code against the rules before you choose the end state.
   1. Read the language page for each file type in scope first.
   2. Take every name in scope through each rule in the index, the language page and the project's own rules.
   3. Names in scope are the folder, each file, class, function, parameter, field and constant.
   4. Take every function body through the same rules.
   5. List the names with a script, not from memory, so none is skipped: Python's `ast`, the TypeScript compiler's API.
   6. Give each name a line: kept, or renamed to what, with the call site that reads it.
   7. Make each finding part of the change, or give it one line on why it stays.
   8. Reasons to stay are the project's own convention, a stored format, or a caller outside scope.
   9. A strict reading not taken is the person's call at approval.
4. Say what the change makes better.
   1. Say what it lets you delete: a branch, an argument threaded through, a one-call wrapper, an impossible state.
   2. Or say what it makes clear: a name that says what it holds or returns, per **rule-name-for-the-reader**.
   3. Add a new model or class only where **rule-typed-boundaries** or **rule-group-by-subject** earns it.
   4. If the change only adds a layer, say that it is not worth doing.
   5. Then stop.
5. Say the end state in plain words.
   1. Give one example of the code after it lands.
   2. Say how many files change.

**Plan mode stops here.** Steps 1 to 5 run during planning. The plan is steps 6 to 14.

6. If the change is more than about five files, Build builds it, not this playbook.
   1. Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/spec.md`.
   2. Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/tickets.md`, with one ticket per part. It ends at the person's approval.
   3. In plan mode, put the spec and the tickets in the plan. Approving the plan is that approval.
   4. Save the spec and the tickets after the approval.
   5. Run `playbooks/build.md` on the spec's folder. This playbook ends here.
   6. When Build's cleanup runs this playbook, skip this step.
   7. In that case, make the edits here.
7. Write each missing test from step 2.
   1. Run it on the code as it is. It passes.
   2. Paste the command and the result.
8. Choose who makes the edits in steps 9 and 10.
   1. When the whole change is under about ten lines, make the edits yourself. Say so in the reply.
   2. Otherwise, hand them to one `general-purpose` subagent with the exact scope.
   3. Give it the files, the names being moved and the promises that must hold.
   4. Also give it the language page for the file type.
9. Remove before you add.
   1. Remove dead code, one-call wrappers (**rule-no-pass-through**) and leftover references.
   2. Then make the smallest change that reaches the end state (**rule-smallest-change**).
10. Move one thing at a time.
   1. Move one thing.
   2. Run the tests.
   3. Move the next thing. Whoever makes the edits runs the tests.
   4. Update every caller and delete the old name in the same move.
   5. Never keep old and new side by side, except across tickets.
   6. Across tickets, the old name stays until the last ticket deletes it.
   7. Grep each rename against strings, docs and tests.
11. Review the diff yourself.
   1. Run the tests yourself.
   2. Paste the command and the result.
   3. Take every name the diff adds or renames through **rule-name-for-the-reader** again, at its call site.
   4. Names include a folder, a file, a class, a function, a parameter, a field, a constant and a test.
   5. Run this check on every refactor, unasked.
   6. Rename a name that fails before the commit.
12. Break it on purpose.
   1. For each moved piece, change one line so it is wrong.
   2. Check that a test fails.
   3. If a test stays green, it was not watching. Write one that does.
   4. Undo the break.
   5. Paste the commands and the results.
13. Ask if the code is easier to read.
   1. Look for fewer functions to keep track of, fewer branches, or one named type where loose values were passed around.
   2. Say which in one line.
   3. If you find none, undo the whole thing.
   4. Say why.
14. Prepare the commits.
   1. Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments.md` on the diff.
   2. Write the commits in order: removal, reshape, cleanup. Give each its message.
   3. Make none unless asked.
   4. When asked, run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/commit.md`.

**Reply:**

- What reads easier, first, and that nothing the person sees changes.
- What moved, and what was deleted.
- The tests that guarded it, and the proof: commands and results, including the break-on-purpose.
- What was undone.
- The commits proposed.
- When step 6 saves the change for Build, the reply at its stop holds three things. They are the spec's path, the ticket list with blockers, and the request to approve.
