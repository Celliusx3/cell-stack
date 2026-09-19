### Investigate

**You own the answer, not the code.** A read-only question ends in a cited answer, never in an edit. If the question turns out to need a change, say so and stop; that is a different playbook.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the question touches them.
2. Locate the code. Grep and glob for the names in the question. If the answer spans more than about five files, spawn one read-only `Explore` subagent per slice with the question and the file list, and read what comes back yourself.
3. Read the files. Trace the actual path through the code, not the docstrings' description of it.
4. Answer from the code with `file:line` on every claim. Anything you did not run is inferred; say so in the same sentence. If a claim can be settled by running something read-only (a test, a script that prints), run it and report the output instead of inferring.
5. Change nothing. No `Edit`, no `Write`, no commit. Name a fix only as a recommendation, marked as one.

**Reply:** the answer first, then the files read with the lines that carry each claim, then what was inferred rather than run.
