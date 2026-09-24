### Fix

**You own the cause, not the symptom. Reproduce, ask why to the root, test first, prove it safe, show it gone on the real surface.** Wrong behaviour only; a feature found on the way is named in the reply and left for its own change.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the fix touches them.
2. Reproduce before reading code. The failure as evidence you can point at: a log line, a request and its reply, a command and its output. State the symptom in one line. A bug you cannot reproduce is not yet a bug; say what you tried.
3. Suspect state before code. Anything that fails after a restart, a deploy or a config change: check config files, caches, lock files, leftovers from a test. A setting that explains the symptom is its own finding and its own fix, and the code bug underneath is still the code bug.
4. Ask why until the answer is a decision, not a line. Trace the symptom to the line that decides, then ask why that line decides so, until the cause is a choice someone made. Grep for the same pattern elsewhere; fix the pattern, not the instance.
5. Decide the fix at the root, here, never inside the code. A guard that silences (a nil check, a catch-all, a default) is a symptom fix. When the fix is a behaviour choice (what to do when X happens), run `/research` (`${CLAUDE_PLUGIN_ROOT}/skills/research/SKILL.md`) on it; a wrong line needs none. Put the fix where the project already puts decisions of that kind: a hook, a policy module, a fold over the log, a validator at the boundary; read the project's own examples of that kind before writing. A fix inlined into the loop's story with its own wording and its own counter is the smallest diff and not the smallest change. Name the one fact the fix is safe because of.
6. Write the regression test and run it. It fails for the bug's reason, not another. Paste the command and the failure. When no cheap test exists, say why and name the closest executable check (a script, a request, a log assertion) instead; prefer no test over a test of mocks.

**Plan mode stops here.** Steps 1 to 6 run during planning; the plan is steps 7 to 11, with the reproduction, the root cause and the safety fact in it.

7. One `general-purpose` subagent writes the fix from the scope: the files, the failing test, the project's `CLAUDE.md`, the language skill for the file type. When the patch is under about ten lines the lead writes it and the reply says so. Review the diff line by line: it is the smallest change that turns the test green.
8. Prove the safety fact by running code, not by writing it up: a test or a script that calls the real thing and fails loud if the fact is false. Say how far it got: pointed at the line, walked the case, ran it, reproduced in the running app.
9. Run the tests. Then reproduce the original failure on the real surface and show it gone; paste what came out. Do not write into the person's live state to prove it: point the config at a scratch directory, or undo what you wrote and say so. "Inconclusive" is not a pass.
10. Two fixes that failed the same check share a wrong premise; question the premise before a third patch.
11. Run `/strip-comments` on the diff. Commits: the test and the fix as one story. Make none unless asked. A wording change goes to the project's prompt ledger when it has one.

**Reply:** what changes for the person, first; the root cause in one line and the symptom it explained; the evidence (the failing test, the passing test, the real surface); the safety fact and how far it was proven; what the next engineer inherits.
