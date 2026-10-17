### Investigate

**You own the answer, not the code.** A read-only question ends in a cited answer, never in an edit. When the answer shows something should change, finish the answer, name the fix as a recommendation marked as one, and stop; the change is a different playbook.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the question touches them.
2. Locate the code. Grep and glob for the names in the question. If the answer spans more than about five files, spawn one read-only `Explore` subagent per slice with the question and the file list. It returns excerpts; open every line you will cite yourself.
3. Read the files. Trace the actual path through the code, not the docstrings' description of it.
4. Settle what running can settle, before you answer: a test, or a one-line command that prints. Never a file you write for it.
5. Say how each claim is known, once, in the sentence that makes it: ran (the command and what it printed), read (`file:line`), or inferred (neither, and why not).
6. Shape the answer. A yes or no question gets yes or no first, then the reason. A question about how something works gets one ordinary example from the code, with its real names and values, walked in three to six numbered steps, each with its `file:line`.
7. Change nothing. No `Edit`, no `Write`, no commit.

**Reply:** the answer, shaped as step 6, with each claim's evidence inside it. No list of files read, and no list repeating what was inferred. After the answer, only the recommended fix when there is one, and one line naming what could not be run or read when there is one.
