# Plan mode

Claude's plan mode and cell mode stack; plan mode wins where they disagree. `/research` runs during planning; the plan carries one line per decision naming who else does it, and the full table goes in the reply, never the plan. In plan mode: match the playbook as usual, run its read-only steps now (reading, tests, naming the shape, the end state), and put the rest into the plan file. Each playbook that writes marks where plan mode stops. After approval, open the todo list and resume the playbook at the first step after that mark; do not redo the read-only steps. Investigate and Explain never write, so plan mode changes nothing for them.

The plan file is written for a person deciding yes or no who has not read the code or the pages the plan changes. Write it in short sentences, one idea in each, in everyday words. A word that needs the codebase to make sense is replaced by the plain one, or explained the first time it appears. No code-like blocks, no before / after tables, no `file:line`, and no line limit: the background the person needs comes before brevity. The plan has three sections, in this order.

## 1. Problem

- **Background first.** One line for each page, part or module the plan touches: what it is for.
- **A short summary of any steps the reader needs**, one plain line per step, so a problem can name a step the reader has just read. For a change to code, the same for what the code does today.
- **Then each problem on its own**, under its own numbered heading: what the page says or the code does today, then one example of what goes wrong (what the person asks, what happens).

## 2. Solution

- **The steps after the change, in short**, one line each, each marked *(same)*, *(new)*, *(was N)* or *(Fix N)*.
- **What each fix does**, numbered like its problem, with the same example: what happens now.
- Each decision in one line: the choice, and who else does it the same way.
- What stays the same, with today's test count ("31 passed"). A promise with no test is named as the first thing to write.
- For a feature: the spec in short, as a numbered walkthrough of a person using it (what they do, what they see). Anything the change stores says where it is kept, in what form, and who can read it. For a refactor saved for Build: its spec in short, saying that nothing the person sees changes.
- A behaviour choice the change exposes and the person must make: the case as one example, what the source being copied does there, and the strict option named.

## 3. How to do it

- **Where the work happens:** the folder and the branch.
- **Before anything:** the checks to run first, and what they show today.
- **Numbered steps:** the playbook's remaining steps, each naming the file it changes. Work over about five files is split into parts, each under its own heading. For a feature, or a refactor saved for Build, the tickets in order, one line each with its blockers, and the folder they are saved in.
- **The checks:** the commands, what passing looks like, and the break-on-purpose for each part.
- **The commits** to suggest, in order.
- **Later:** what is left for separate changes, one line each, saying why nothing here changes for it.
