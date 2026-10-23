# Plan mode

Claude's plan mode and cell mode stack. Where they disagree, plan mode wins. `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research.md` runs during planning. The plan carries one line per decision, naming who else does it. The full research table goes in the reply, never in the plan.

In plan mode, match the playbook as usual. Run its read-only steps now: reading, tests, naming the shape, the end state. Put the rest into the plan file. Each playbook that writes marks where plan mode stops.

After approval, open the todo list. Resume the playbook at the first step after that mark. Do not redo the read-only steps. Investigate and Explain never write, so plan mode changes nothing for them.

The plan file is for a person who decides yes or no and has not read the code or the pages the plan changes. Write it per the mode's Writing section. Replace a word that needs the codebase to make sense with the plain one, or explain it the first time it appears. Use no tables, no `file:line`, and no quotes from the page or the code being changed. Say what the page or the code makes happen instead.

The one code block is the layout in section 4. Only section 4 uses the code's own names as they are. The whole plan follows one example. Section 1 picks it, sections 2 and 3 walk it again, and section 4 shows its changed line. The plan has five sections, in this order.

Before `ExitPlanMode`, run `${CLAUDE_PLUGIN_ROOT}/scripts/long-sentences.py` with the plan file's path. Fix each sentence it prints.

## 1. What it is

- **One example, walked in numbered steps:** what the person does, what Claude or the code does, and what happens. One action happens in each step. Use real names and values, small enough to need no explaining.
- **Then one line:** so this is what it is, and this is what the plan changes.

## 2. Today's flow

- **The same example, walked through how things work now**, in numbered steps.
- Each step has two labelled parts: what the code does, and what is wrong with it. Give one problem per bullet. Say what goes wrong in the step where it happens, as what the person would see.
- Use real values, not a stated rule. Give the id or name the code is handed and what it gives back (`r1` in, `r1` out). Never write a sentence of the form "the X is the Y".
- A risk is a short story: the change someone makes, what then breaks, and what the person sees.
- Tell a rule kept in two places as the two questions it answers, each with where it is asked. The story walks through both.
- A problem the example does not reach gets one closing line, with its own small example.
- For a feature, today's flow is what the person does now without it. For a refactor, the flow opens with one line that says none of it shows in the app. Each step is then about the next person who reads or changes the code.

## 3. The flow after the change

- **The same example, with the same step numbers**, walked through how things will work. A step that is the same says so. Where the person approves, the flow says so.
- Each decision in one line: the choice, and who else does it the same way.
- What stays the same, with today's test count ("31 passed"). Name a promise with no test as the first thing to write.
- For a feature, say where the change keeps anything it stores, in what form, and who can read it. For a refactor saved for Build, say that nothing the person sees changes. The flow is then a person reading or changing the code.
- A behaviour choice the change exposes, which the person must make, gets three parts. Give the case as one example. Say what the source being copied does there. Name the strict option.
- For a refactor, the section ends with the rules check from the Refactor playbook. Give one line per finding: what is renamed, which ticket fixes it, or why it stays. Mark a strict reading not taken as to decide at approval.

## 4. The changes

This section shows what the diff will hold, in one place. The person sees it without walking sections 2 and 3 again. It is for a reader who knows the code, so it names files and functions as they are.

- **The example's line, before and after:** the one import or call from the example that changes, with its real names.
- **The layout, before and after,** as one tree in a code block. The tree shows every folder and file that changes, each with the names it holds. The old is on the left of an arrow, and the new is on the right. A new file says it is new, and a removed file says where its names went. A folder that keeps its layout gets one line that says so. For a feature, the tree shows each new file and what it holds.
- **Each rename, old to new,** with the line that calls it before and after. The person then judges the name where it is read.
- **What follows:** the files that change only an import or a line, as counts ("21 app files"), and each doc that names an old path.
- **What does not change,** in one line, with today's test count.

## 5. How to do it, in short

Give each item one line, except the steps.

- **Where the work happens:** the folder and the branch.
- **Before anything:** the checks to run first, and what they show today.
- **The steps:** the playbook's remaining steps, as a numbered list with one action in each step. Each step names the file it changes. Split work over about five files into parts. For a feature, or a refactor saved for Build, list the tickets in order with their blockers, and the folder they are saved in.
- **The checks:** the commands, what passing looks like, and the break-on-purpose for each part.
- **The commits** to suggest, in order.
- **Later:** what is left for separate changes, and why nothing here changes for it.
