### Feature

**You own the design. Research, decide, review, verify. A subagent writes the code.** New behaviour only; a bug found on the way is named in the reply and left for its own change.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. Read the code the feature touches and its tests. Name the data shape it changes or adds, per **rule-typed-boundaries** and **rule-group-by-subject**, before anything else is decided.
3. Run `/research` (`${CLAUDE_PLUGIN_ROOT}/skills/research/SKILL.md`) on the question. Its table goes in the reply.
4. Decide the design here, never inside the code: the end state as one story block (the shape in the mode's Plan mode section), and the alternatives as a table with the pick and why. A design that crosses more than about five files is two features; do the first.
5. Write the test that describes the new behaviour and run it. It fails. Paste the command and the failure.

**Plan mode stops here.** Steps 1 to 4 run during planning; the plan is steps 5 to 8, with the research table and the design in it.

6. Hand the code to one `general-purpose` subagent with the exact scope: the files, the data shape and its class, the failing test that must pass, the project's `CLAUDE.md`, and the language skill for the file type. You do not write the code. Review its diff line by line. Send it back with the exact failure rather than patching it yourself, unless the patch is one line.
7. Run the tests yourself. Then run the real thing on its own surface (the endpoint, the command, the page) and paste what came out. "Inconclusive" is not a pass; say what was not verified.
8. Run `/strip-comments` on the diff. Write the commits in order, each with its message. Make none unless asked.

**Reply:** what changes for the person using it, first; then what the next engineer inherits; the research table; the design pick with its alternatives; the evidence (commands and output); open decisions.
