### Fix

**You own the cause, not the symptom. The wrong behaviour goes away and nothing else changes.** A feature or a cleanup found on the way is named in the reply and left for its own change.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules.
   1. If the fix touches the rule files it links, open them.
2. Reproduce before reading code, on a scratch config, never the person's live state.
   1. Point the config at a scratch directory.
   2. If you wrote to the live state, undo what you wrote. Say that you did.
   3. Keep the failure as evidence you can point at. Evidence is a log line, a request and its reply, or a command and its output.
   4. State the symptom in one line.
   5. If you cannot reproduce the bug, it is not yet a bug. Say what you tried.
3. Suspect state before code.
   1. If anything fails after a restart, a deploy or a config change, check the state first.
   2. The state is config files, caches, lock files and leftovers from a test.
   3. If a setting explains the symptom, name it.
   4. Fix the setting where it lives, with the person. Never code around it.
   5. If the symptom is still there once the setting is fixed, go on to the code.
4. Trace the symptom to the line that causes it.
   1. Ask why that line is wrong.
   2. A plain mistake ends the search: a wrong operator, or a line that adds twice.
   3. Trace a choice about what to do in some case to where it was made.
   4. Grep for the same mistake elsewhere.
   5. Fix each copy in this change.
   6. Name anything else in the reply.
5. Decide the fix at the cause.
   1. Never fix it with a guard that hides the symptom: a nil check, a catch-all, a default.
   2. When the fix is a behaviour choice (what to do when X happens), run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research.md` on it.
   3. Put the fix where the project already keeps that kind of decision.
   4. That place is a validator where data comes in, a policy module, or a hook.
   5. Read one of the project's own examples first.
   6. A smaller diff that breaks a house rule is not a saving, per **rule-smallest-change**.
6. Say in one line why the fix is safe.
   1. Name the one thing that must stay true so the fix breaks nothing else.
   2. Name the regression test: where it goes, what it checks, and which reproduction from step 2 it turns into.
   3. Write nothing yet.
   4. When no cheap test exists, say why.
   5. Then name the closest check that runs: a script, a request, a log assertion.
   6. Prefer no test over a test of mocks.

**Plan mode stops here.** Steps 1 to 6 only read and run. Nothing on disk changes. The plan is the fix: the reproduction, the cause, the change, why it is safe, and the test. Steps 7 to 11 follow it.

7. Write the test.
   1. Run it. It fails for the bug's reason, not another.
   2. Paste the command and the failure.
8. Make the fix.
   1. When the fix is under about ten lines, write it yourself. Say so in the reply.
   2. Otherwise, hand it to one `general-purpose` subagent with the exact scope.
   3. Give it the files, the failing test, the project's `CLAUDE.md` and the language page for the file type.
   4. Review the diff. Every line traces to the bug, per **rule-smallest-change**, and the test turns green.
9. Prove why the fix is safe by running code.
   1. Use a test or a script that calls the real thing and fails if the reason is false.
   2. When it cannot be run, say how far you got: pointed at the line, or walked the case by hand.
   3. Say that it is not proven.
10. Run the tests.
   1. Show the original failure gone on the surface the person uses, on the scratch config from step 2.
   2. Paste what came out.
   3. For a page, open it in a browser and click through it. A request to the server does not count.
   4. Follow the repo's `how-to-use-*` skill.
   5. If the repo has none, write one first with `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/write-how-to-use.md`.
   6. "Inconclusive" is not a pass.
   7. When a second fix fails the same check, stop. The two fixes share a wrong assumption.
   8. Go back to step 4.
11. Finish the diff.
   1. Run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments.md` on the diff.
   2. Plan the test and the fix as one commit story.
   3. Make no commit unless asked.
   4. When asked, run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/commit.md`.
   5. When the fix changes text a model follows, record the change in the project's prompt ledger.
   6. Text a model follows is a prompt or a tool description, per **rule-name-tools-exactly**.

**Reply:**

- What changes for the person, first.
- The cause in one line, and the symptom it explained.
- The evidence: the test failing then passing, and the surface the person uses, each with its command and result.
- Why the fix is safe, and how far that was proven.
- Anything found on the way and left for its own change.
- What the next engineer inherits.
