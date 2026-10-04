### POC

**You own a working slice the person can see, not finished code.** The first stage of a Feature, or the whole task when the person asks to try or prototype something: make the new behaviour work end to end on the real surface with the least code. Names, shape, a test per promise and comments wait for Refactor and Clean up. The POC's code is the draft they work on; it is never thrown away.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. Read the code the slice touches and its tests. Name the data shape it adds or changes, per **rule-typed-boundaries**, and where each new file goes, per **rule-place-by-kind**.
3. Run `/research` (`${CLAUDE_PLUGIN_ROOT}/skills/research/SKILL.md`) on the question. Its table goes in the reply.
4. Pick the slice: the shortest path from what the person does to what they see, as one story block, and the alternatives as a table with the pick and why. More than about five files is two slices; build the first.
5. Write one end-to-end check of that path through the real entry point (a test, or the repo's drive script) and run it. It fails. Paste the command and the failure.

**Plan mode stops here.** Steps 1 to 5 run during planning; the plan is steps 6 to 9.

6. Hand the slice to one `general-purpose` subagent with the exact scope: the files, the data shape, the failing check, the project's `CLAUDE.md`, the language skill for the file type. You write any text a model will follow, per **rule-spell-the-call**. Review its diff for what it does; a name or a shape you would change goes on the rough-spots list, not back to the subagent.
7. Run the tests, then drive the slice on the surface the person uses, on a scratch config: follow the repo's `drive-*` skill, or run `/drive` first. A bug that blocks the slice is fixed now as its own Fix, with its own test. A failure the environment causes (a server setting, a model's window, a missing key) is named and fixed where it lives, with the person; it is never coded around.
8. Write the rough-spots list from your own review: a name that needs its docstring, two words for one thing, a function past the length cap, a promise with no test, anything shaped for the slice rather than the codebase. It is Refactor's input.
9. Leave the app running on the person's setup with numbered steps to try it, and stop. Refactor starts when they say it works, or right away when the request already asked for the finished change (a commit, a PR).

**Reply:** what the person can try now, as numbered steps; the evidence (the check red, then green, and what the drive showed); each finding and what fixed it; the rough-spots list; the research table and the pick; then one question: does it work for you, so Refactor can start?
