### Explain

**You own the reader's understanding, not the code.** A request to explain ends in everyday words and one example, never in an edit and never in a cited trace. Citations are your evidence, not the reader's reading; they stay out of the body. If explaining turns up a defect, name it and stop; that is a different playbook.

1. Apply the project's `CLAUDE.md` (already in context) as this repo's principles; open the rule files it links if the subject touches them.
2. Pin the subject and the reader. Assume the reader has not read the code and does not want to.
3. Read the real mechanism. Grep and glob for the subject; prefer its tests and callers over its definition. If they span more than about five files, spawn one read-only `Explore` subagent per slice and read what comes back yourself. Run anything runnable so the numbers in the reply are real. This is evidence for you; none of it is pasted into the reply.
4. The problem, in two sentences: what goes wrong without this thing, in the reader's terms.
5. The one idea, in two sentences: the single distinction or picture that makes the rest follow, then an everyday analogy for it.
6. The mechanism, as two to four bullets of one sentence each. One of them is a concrete example: this input, this comes out.
7. The gotcha, in one sentence: the case that looks like the thing but is not.
8. End with one question: which part lost you.
9. When the reader names a part, explain only that part one level deeper: the two sides it was hiding, numbered, one example that walks through both, the same question again. Same words, same cap.
10. Change nothing. No `Edit`, no `Write`, no commit. Name a fix only as a recommendation, marked as one.

**Words:** the ones a person who does not program would use. No stream, yield, terminal, generator, subscriber, drain, protocol. A thing the code calls out is written as what it would say, in quotes: "I'm finished", "I'm waiting for you". A code name appears only when the reader will have to type it, once, in backticks.

**Reply:** problem, one idea, mechanism, gotcha, question. Twenty lines is the cap; every part is at its stated length or shorter, and there is no file list, no `file:line`, no closing summary. The cited trace is what Investigation is for; offer it only when asked.
