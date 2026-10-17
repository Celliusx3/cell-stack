### Feature

**New behaviour, planned with the person in four stages: grill, research, spec, tickets.** It stops twice: after the grill, so the person confirms what they want, and after the tickets, so they approve the spec and the split. Then Build runs. A bug found on the way is its own Fix, with its own test and commit.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. Read the code the change touches and its tests, so no question asks what the code answers. Name the data shape it adds or changes, per **rule-typed-boundaries**, and where each new file goes, per **rule-place-by-kind**.
3. **Grill.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/grill.md`: rounds of numbered questions about what the person wants and why, each with a recommended answer. Stop 1 is the person confirming the agreed answers.
4. **Research.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research.md` on how others build what was agreed. Its table goes in the reply.

**Plan mode stops here.** Steps 1 to 4 run during planning. The plan carries the spec and the ticket list as steps 5 and 6 would write them, and approving the plan is stop 2; after approval, save them and go on to step 7.

5. **Spec.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/spec.md`.
6. **Tickets.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/tickets.md`. Stop 2 is the person approving the spec and the tickets.
7. **Build.** After approval, run `playbooks/build.md` on the spec's folder straight away, unless the person says to build later.

**Reply:** at stop 1, the grill's agreed answers and the request to confirm. At stop 2: the spec's path, the research table and the pick, the ticket list with blockers, the decisions left open, and the request to approve.
