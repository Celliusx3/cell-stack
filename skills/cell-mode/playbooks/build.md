### Build

**Build a saved spec's tickets in order, then clean up, without stopping.** The input is a spec folder the Feature or Refactor playbook wrote, or one the person points at. Each ticket is committed as it passes. Nothing is pushed or merged until the person asks. A bug found on the way is its own Fix, with its own test and commit.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules.
   1. If the change touches the rule files it links, open them.
2. Read the spec and every ticket in its folder.
   1. Build the `open` tickets in number order.
   2. Let a ticket whose blockers are not `done` wait.
   3. Put all of it on one branch for the feature, written where the mode says longer work goes.
3. For each ticket, write its Checks as one end-to-end check through the real entry point.
   1. Use a test, or the repo's how-to-use skill, as the entry point.
   2. Run the check. It fails.
   3. Paste the command and the failure.
   4. For a refactor ticket, nothing fails first, because it changes no behaviour.
   5. Instead, run the tests that guard its promises.
   6. Paste them green.
   7. After step 5, break each moved piece on purpose.
   8. Check that a test fails.
   9. Undo the break.
4. Hand the ticket to one `general-purpose` subagent with the exact scope.
   1. Give it the ticket file, the spec, the data shape and the check from step 3.
   2. Also give it the project's `CLAUDE.md` and the language page for the file type.
   3. Write any text a model will follow yourself, per **rule-name-tools-exactly**.
   4. Review its diff for what it does.
   5. Put a name or a shape you would change on the rough-spots list.
5. Prove that the ticket works.
   1. Run the tests.
   2. Try the ticket on the surface the person uses, on a scratch config.
   3. Follow the repo's `how-to-use-*` skill.
   4. If the repo has none, write one first with `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/write-how-to-use.md`.
   5. Fix a bug that blocks the ticket now, as its own Fix with its own test.
   6. Name a failure that the environment causes: a server setting, a model's window, a missing key.
   7. Fix that failure where it lives, with the person. Never code around it.
6. Commit the ticket.
   1. Set the ticket's Status to `done`.
   2. Commit the ticket with `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/commit.md`. The person's approval of the tickets covers this commit.
   3. Start the next ticket, with no stop in between.
7. **Make it right.** Run a refactor on the whole feature.
   1. Write the rough-spots list from your own review. It holds:
      - every name the build added or renamed, read at its call site per **rule-name-for-the-reader**
      - a name that needs its docstring
      - two words for one thing
      - a function past the length cap
      - a promise with no test
      - anything shaped for one ticket rather than the codebase
   2. Run `playbooks/refactor.md` straight away, with the feature's whole diff as the scope and the list as the candidates.
   3. Let it write a test for every promise that has none, before anything moves.
   4. Skip Refactor's hand-off to Build. Make its edits inside this Build, never in a second one.
8. **Make it clean.** Check the whole diff before the last commit.
   1. Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments.md` on the whole diff.
   2. Check every ticket's Checks and the spec's "How we will know it works" against the final code.
   3. Fix what fails.
   4. Update the docs the change made wrong: the project's plan, its prompt ledger, a how-to-use skill's feature map.
   5. Run the tests on the final code.
   6. Try it once more on the final code.
   7. Paste both results.
9. Commit the cleanup with `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/commit.md` as the last commit.
   1. Push, merge or open a PR only when the person asks.
   2. Write the PR text per the mode's Writing section.

**Reply:**

- What changes for the person, as numbered steps they can try. For a refactor, say that nothing they see changes, and what reads easier.
- Per ticket: its check red then green, what trying it showed, and its commit. A refactor ticket's check is green before and after, with its break.
- Each finding, and what fixed it.
- What the refactor moved, and the break-on-purpose results.
- The final run.
- What the next engineer inherits.
- The decisions left open.
