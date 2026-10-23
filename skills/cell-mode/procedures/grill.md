# Grill

Question the person about a feature until nothing about what they want is open or quietly assumed. The spec is written from the agreed answers. Shaped after mattpocock's grilling skill.

## Steps

1. Sort every open question by who can answer it. Evidence: the questions you answered from the code, one line each with the file.
   1. Read what exists today from the code: a field, a command, how something is stored. Never ask it.
   2. Leave how others build this kind of thing for research.
   3. Send what the person wants, and why, to the person.
2. Ask one round of questions.
   1. Ask, in a numbered list and in their words, every question about what they want that you can see now.
   2. Make each one a yes-or-no question whose "yes" is your recommended answer. A plain "yes" then accepts it.
   3. After each question, write that answer out after "Recommended:".
   4. Write each question per the mode's Writing section.
   5. Ask nothing about how it will be built: files, modules, layout.
   6. Show no design yet. The design comes after the grill.
   7. When `AskUserQuestion` is available, use it, with four questions to a call.
   8. In each call, put the recommended option first, with "(Recommended)" in its label.
   9. When `AskUserQuestion` is not available, write the numbered list in the reply.
   10. End the turn after the list.
3. Read the answers.
   1. When an answer opens new questions, start the next round. Ask only what that answer opened.
   2. When the person uses a word loosely, propose one exact word for it in the next round.
   3. Use only that word afterwards.
4. Stop when nothing is open and nothing is assumed.
   1. List the agreed answers, numbered, one line each.
   2. Ask the person to confirm them. This is stop 1. Nothing is written until they confirm.
5. When the person says not to ask ("don't ask", "just go", "no questions"), ask nothing.
   1. Take your recommended answers.
   2. Mark each one as an assumption, for the spec to list.

## Reply

Each round gives what you read from the code instead of asking, one line each. Then it gives the numbered questions, each with its "Recommended:" answer. A defect found on the way is one line after the questions. At the end, the reply gives the agreed answers, numbered, and the request to confirm them.
