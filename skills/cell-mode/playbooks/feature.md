### Feature

**New behaviour, in three stages run back to back: make it work, make it right (Refactor), make it clean (Clean up).** The working code is reshaped, never rewritten, and no stage waits for the person to approve the one before. A bug found on the way is its own Fix, with its own test and commit.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. Read the code the change touches and its tests. Name the data shape it adds or changes, per **rule-typed-boundaries**, and where each new file goes, per **rule-place-by-kind**.
3. Run `/research` (`${CLAUDE_PLUGIN_ROOT}/skills/research/SKILL.md`) on the question. Its table goes in the reply.
4. Pick the slice: the shortest path from what the person does to what they see, as one story block, and the alternatives as a table with the pick and why. More than about five files is two slices; build the first.
5. Write one end-to-end check of that path through the real entry point (a test, or the repo's drive script) and run it. It fails. Paste the command and the failure.

**Plan mode stops here.** Steps 1 to 5 run during planning; the plan is steps 6 to 10.

6. **Make it work.** Hand the slice to one `general-purpose` subagent with the exact scope: the files, the data shape, the failing check, the project's `CLAUDE.md`, the language skill for the file type. You write any text a model will follow, per **rule-spell-the-call**. Review its diff for what it does; a name or a shape you would change goes on the rough-spots list.
7. Run the tests, then drive the slice on the surface the person uses, on a scratch config: follow the repo's `drive-*` skill, or run `/drive` first. A bug that blocks the slice is fixed now as its own Fix, with its own test. A failure the environment causes (a server setting, a model's window, a missing key) is named and fixed where it lives, with the person; it is never coded around.
8. **Make it right.** Write the rough-spots list from your own review: a name that needs its docstring, two words for one thing, a function past the length cap, a promise with no test, anything shaped for the slice rather than the codebase. Then run `playbooks/refactor.md` with this change's diff as the scope and the list as the candidates, straight away. Its step 2 writes a test for every promise before anything moves; step 5 wrote only the end-to-end check.
9. **Make it clean.** Run `/strip-comments` on the whole diff. Update the docs the change made wrong: the project's plan, its prompt ledger, a drive skill's feature map. Run the tests and the drive once more on the final code, and paste both.
10. Write the commits in order: each Fix, then the feature with its refactor folded in, then the docs, each with its message. Make none unless asked; when asked, run `/commit`, and open a PR only when asked.

**Reply:** what changes for the person, as numbered steps they can try; the evidence (the check red, then green, what the drive showed, the final run); each finding and what fixed it; what the refactor moved and the break-on-purpose results; the research table and the pick; what the next engineer inherits; the commits proposed; open decisions.
