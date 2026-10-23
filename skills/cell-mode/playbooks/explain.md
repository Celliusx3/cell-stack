### Explain

**You own the reader's understanding, not the code.** A request to explain ends in a short problem and one example walked from start to end, in everyday words. It never ends in an edit, and never in a cited trace. Citations are your evidence, not the reader's reading. They stay out of the body.

If explaining turns up a defect, name it. Then stop. That is a different playbook.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's rules.
   1. If the subject touches the rule files it links, open them.
2. Say what is being explained and to whom.
   1. Assume the reader has not read the code and does not want to.
3. Read the real mechanism.
   1. Grep and glob for the subject.
   2. Prefer its tests and callers over its definition.
   3. If they span more than about five files, spawn one read-only `Explore` subagent per slice.
   4. Read what comes back yourself.
   5. Run anything runnable, so the numbers in the reply are real.
   6. This is evidence for you. None of it is pasted into the reply.
4. Pick one example from what you read.
   1. Pick the most ordinary thing a person does that passes through the subject, not an edge case.
   2. Use its real names and values, small enough to need no explaining of its own.
5. **Problem.** Open with one line saying what the subject does, in plain words.
   1. Then write two or three sentences on what goes wrong without this thing.
   2. Tell it as what the person sees or has to do.
6. **Explanation.** Walk the example as numbered steps, three to six, each short.
   1. Each step says what goes in, what this thing does with it, and what comes out.
   2. Leave out a step that does not change what comes out: reading, choosing, preparing.
   3. A step never stops to explain a second thing.
   4. Explain a new word inside the step that first needs it.
   5. Use no analogy, no list of parts, and no summary after the steps. The example carries all of it.
7. When the reader asks about one step, explain only that step, one level deeper, in the same shape.
   1. Give the problem that step solves, in one sentence.
   2. Walk that step as its own smaller example.
8. When the reader says they do not understand and names no step, start over.
   1. Use a smaller example and fewer steps.
   2. When a comparison from outside software fits, it may open the explanation.
   3. Examples are a form at a counter, or a key that only opens one door.
9. Change nothing. No `Edit`, no `Write`, no commit.
   1. Name a fix only as a recommendation, marked as one.

**Words:** the ones a person who does not program would use. Do not use stream, yield, terminal, generator, subscriber, drain or protocol. Write a thing the code calls out as what it would say, in quotes: "I'm finished", "I'm waiting for you". Use a code name only when the reader will have to type it, once, in backticks.

**Reply:**

- Problem, then Explanation.
- Nothing after the steps but one line naming a defect found on the way, or something you could not run, when there is one.
- Fifteen lines is the cap.
- No file list, no `file:line`, and no closing summary.
- The cited trace is what Investigate is for. Offer it only when asked.
