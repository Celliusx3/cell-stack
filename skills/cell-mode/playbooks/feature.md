### Feature

**New behaviour, in three stages: make it work (POC), make it right (Refactor), make it clean (Clean up).** The POC's code is kept and reshaped, never rewritten. A bug found on the way is its own Fix, with its own test and commit.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the change touches them.
2. **POC.** Run `playbooks/poc.md` to its end. It stops with the slice running on the person's setup, one end-to-end check green, and a rough-spots list.
3. **Refactor.** When the person says it works, or the request already asked for the finished change, run `playbooks/refactor.md` with the POC's diff as the scope and its rough-spots list as the candidates. Its step 2 writes a test for every promise before anything moves; the POC wrote only the end-to-end check.
4. **Clean up.** Run `/strip-comments` on the whole diff. Update the docs the change made wrong: the project's plan, its prompt ledger, a drive skill's feature map. Run the tests and the drive once more on the final code, and paste both.
5. Write the commits in order: each Fix, then the feature with its refactor folded in, then the docs, each with its message. Make none unless asked; when asked, run `/commit`, and open a PR only when asked.

**Plan mode stops here** inside the POC: its steps 1 to 5 run during planning, and the plan is the rest of the POC.

**Reply:** at the end of each stage, that stage's reply. After Clean up: what changes for the person, what the next engineer inherits, the evidence from the final run, the commits proposed, open decisions.
