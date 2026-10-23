### Investigate

**You own the answer, not the code.** A read-only question ends in a cited answer, never in an edit. When the answer shows something should change, finish the answer. Name the fix as a recommendation, marked as one. Then stop. The change is a different playbook.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules.
   1. If the question touches the rule files it links, open them.
2. Locate the code.
   1. Grep and glob for the names in the question.
   2. If the answer spans more than about five files, spawn one read-only `Explore` subagent per slice.
   3. Give each subagent the question and the file list.
   4. It returns excerpts. Open every line you will cite yourself.
3. Read the files.
   1. Trace the actual path through the code, not the docstrings' description of it.
4. Settle what running can settle, before you answer.
   1. Run a test, or a one-line command that prints.
   2. Never write a file for it.
5. Say how each claim is known, once, in the sentence that makes it:
   - ran: the command and what it printed
   - read: `file:line`
   - inferred: neither, and why not
6. Shape the answer.
   1. Answer a yes or no question with yes or no first, then the reason.
   2. Answer a question about how something works with one ordinary example from the code, with its real names and values.
   3. Walk that example in three to six numbered steps, each with its `file:line`.
7. Change nothing. No `Edit`, no `Write`, no commit.

**Reply:**

- The answer, shaped as step 6, with each claim's evidence inside it.
- No list of files read, and no list repeating what was inferred.
- After the answer, only the recommended fix when there is one.
- Then one line naming what could not be run or read, when there is one.
