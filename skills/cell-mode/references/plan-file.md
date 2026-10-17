# Plan mode

Claude's plan mode and cell mode stack; plan mode wins where they disagree. `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research.md` runs during planning; the plan carries one line per decision naming who else does it, and the full table goes in the reply, never the plan. In plan mode: match the playbook as usual, run its read-only steps now (reading, tests, naming the shape, the end state), and put the rest into the plan file. Each playbook that writes marks where plan mode stops. After approval, open the todo list and resume the playbook at the first step after that mark; do not redo the read-only steps. Investigate and Explain never write, so plan mode changes nothing for them.

The plan file is written for a person deciding yes or no who has not read the code or the pages the plan changes. Write it in short sentences, one idea in each, in everyday words. A word that needs the codebase to make sense is replaced by the plain one, or explained the first time it appears. No code-like blocks, no tables, no `file:line`, and no quotes from the page or the code being changed: say what it makes happen instead. The whole plan follows one example, picked in section 1 and walked again in sections 2 and 3. The plan has four sections, in this order.

## 1. What it is

- **One example, walked in numbered steps:** what the person does, what Claude or the code does, what happens. Use real names and values, small enough to need no explaining.
- **Then one line:** so this is what it is, and this is what the plan changes.

## 2. Today's flow

- **The same example, walked through how things work now**, in numbered steps.
- What goes wrong is said in the step where it happens, as what the person would see.
- A problem the example does not reach gets one closing line, with its own small example.
- For a feature, today's flow is what the person does now without it.

## 3. The flow after the change

- **The same example, with the same step numbers**, walked through how things will work. A step that is the same says so. Where the person approves, the flow says so.
- Each decision in one line: the choice, and who else does it the same way.
- What stays the same, with today's test count ("31 passed"). A promise with no test is named as the first thing to write.
- For a feature: anything the change stores says where it is kept, in what form, and who can read it. For a refactor saved for Build: that nothing the person sees changes, and the flow is a person reading or changing the code.
- A behaviour choice the change exposes and the person must make: the case as one example, what the source being copied does there, and the strict option named.

## 4. How to do it, in short

One line each:

- **Where the work happens:** the folder and the branch.
- **Before anything:** the checks to run first, and what they show today.
- **The steps:** the playbook's remaining steps, each naming the file it changes. Work over about five files is split into parts. For a feature, or a refactor saved for Build, the tickets in order with their blockers, and the folder they are saved in.
- **The checks:** the commands, what passing looks like, and the break-on-purpose for each part.
- **The commits** to suggest, in order.
- **Later:** what is left for separate changes, saying why nothing here changes for it.
