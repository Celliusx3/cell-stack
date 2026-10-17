# Grill

Question the person about a feature until nothing about what they want is left open or quietly assumed. The agreed answers are what the spec is written from. Shaped after mattpocock's grilling skill.

## Steps

1. Sort every open question by who can answer it. What exists today (a field, a command, how something is stored) is read from the code and never asked. How others build this kind of thing is left for research. What the person wants, and why, goes to the person. Evidence: the questions you answered from the code, one line each with the file.
2. Ask one round: every question about what the person wants that you can see now, numbered, in their words. Each is a yes-or-no question whose "yes" is your recommended answer, so a plain "yes" accepts it, and each is followed by that answer written out after "Recommended:". Ask nothing about how it will be built (files, modules, layout) and show no design yet; that comes after the grill. When `AskUserQuestion` is available, use it, four questions to a call, with the recommended option first and "(Recommended)" in its label. Otherwise write the numbered list in the reply and end the turn there.
3. Read the answers. An answer that opens new questions starts the next round, which asks only what it opened. When the person uses a word loosely, propose one exact word for it in the next round and use only that word afterwards.
4. Stop when nothing is open and nothing is assumed. List the agreed answers, numbered, one line each, and ask the person to confirm them. This is stop 1: nothing is written until they confirm.
5. When the person says not to ask ("don't ask", "just go", "no questions"), ask nothing. Take your recommended answers and mark each one as an assumption, for the spec to list.

## Reply

Each round: what you read from the code instead of asking, one line each, then the numbered questions, each with its "Recommended:" answer. A defect found on the way is one line after the questions. At the end: the agreed answers, numbered, and the request to confirm them.
