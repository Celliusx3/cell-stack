### Feature

**New behaviour, planned with the person in four stages: grill, research, spec, tickets.** It stops twice. The first stop comes after the grill, so the person confirms what they want. The second comes after the tickets, so they approve the spec and the split. Then Build runs. A bug found on the way is its own Fix, with its own test and commit.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules.
   1. If the change touches the rule files it links, open them.
2. Read the code the change touches and its tests, so no question asks what the code answers.
   1. Name the data shape it adds or changes, per **rule-typed-boundaries**.
   2. Name where each new file goes, per **rule-place-by-kind**.
3. **Grill.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/grill.md`.
   1. Ask rounds of numbered questions about what the person wants and why, each with a recommended answer.
   2. Stop 1 is the person confirming the agreed answers.
4. **Research.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research.md` on how others build what was agreed. Its table goes in the reply.

**Plan mode stops here.** Steps 1 to 4 run during planning. The plan carries the spec and the ticket list as steps 5 and 6 would write them. Approving the plan is stop 2. After approval, save the spec and the tickets. Then go on to step 7.

5. **Spec.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/spec.md`.
6. **Tickets.** Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/tickets.md`. Stop 2 is the person approving the spec and the tickets.
7. **Build.** After approval, run `playbooks/build.md` on the spec's folder straight away, unless the person says to build later.

**Reply:**

- At stop 1: the grill's agreed answers, and the request to confirm them.
- At stop 2: the spec's path, the research table and its pick, and the ticket list with blockers.
- Also at stop 2: the decisions left open, and the request to approve.
