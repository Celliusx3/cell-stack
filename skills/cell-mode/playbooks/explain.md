### Explain

**You own the reader's understanding, not the code.** A request to explain ends in a short problem and one example walked from start to end, in everyday words, never in an edit and never in a cited trace. Citations are your evidence, not the reader's reading; they stay out of the body. If explaining turns up a defect, name it and stop; that is a different playbook.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules; open the rule files it links if the subject touches them.
2. Say what is being explained and to whom. Assume the reader has not read the code and does not want to.
3. Read the real mechanism. Grep and glob for the subject; prefer its tests and callers over its definition. If they span more than about five files, spawn one read-only `Explore` subagent per slice and read what comes back yourself. Run anything runnable so the numbers in the reply are real. This is evidence for you; none of it is pasted into the reply.
4. Pick one example from what you read: the most ordinary thing a person does that passes through the subject, with its real names and values, small enough to need no explaining of its own. Not an edge case.
5. **Problem.** Open with one line saying what the subject does, in plain words. Then two or three sentences: what goes wrong without this thing, told as what the person sees or has to do.
6. **Explanation.** Walk the example as numbered steps, three to six, each short: what goes in, what this thing does with it, what comes out. A step that does not change what comes out (reading, choosing, preparing) is left out, and a step never stops to explain a second thing. A new word is explained inside the step that first needs it. No analogy, no list of parts, no summary after the steps; the example carries all of it.
7. When the reader asks about one step, explain only that step one level deeper, in the same shape: the problem that step solves, in one sentence, then that step walked as its own smaller example.
8. When the reader says they do not understand and names no step, start over with a smaller example and fewer steps. A comparison from outside software may open it when one fits (a form at a counter, a key that only opens one door).
9. Change nothing. No `Edit`, no `Write`, no commit. Name a fix only as a recommendation, marked as one.

**Words:** the ones a person who does not program would use. No stream, yield, terminal, generator, subscriber, drain, protocol. A thing the code calls out is written as what it would say, in quotes: "I'm finished", "I'm waiting for you". A code name appears only when the reader will have to type it, once, in backticks.

**Reply:** Problem, then Explanation, and nothing after the steps but one line naming a defect found on the way or something you could not run, when there is one. Fifteen lines is the cap, and there is no file list, no `file:line`, no closing summary. The cited trace is what Investigate is for; offer it only when asked.
