---
name: cell-mode
description: The front door for any task that needs rigor. Matches the task to a playbook, runs it with the project's own rules attached, and ends with evidence you can check. Use for /cell-mode or "work in cell mode".
disable-model-invocation: true
---

# Cell mode

## Sticky

Claude Code has no mode concept, so this skill is sticky by instruction. It arrives at session start through the plugin's hook, or when someone types `/cell-mode`; either way it stays on for the rest of the conversation. A new task, a playbook match, or a need for rigor means apply it in full. A casual turn means stay out of the way. "new task" means re-match a playbook instead of continuing the prior one. The user opts out by saying so.

## Resolving a skill

Every skill in this plugin is user-invocable only, so it is not in your Skill listing. It lives at `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md`. Read that file in full before applying it. Playbook paths below are relative to `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/`.

## Every task starts the same way

The project's own `CLAUDE.md` is already in your context. Before anything else, read the files it points at for rules (a `docs/rules.md`, a `DESIGN.md`) when the task touches them. Its rules and invariants bind this repo. Cite them the way you cite a rule below: by the rule's own words, with the file it came from. Project rules live in the project, not here.

Any code you write: no narration comments. A comment survives only under the five exceptions in `/strip-comments`, or the project's own comment rule where it has one. Before you hand back a diff, run `/strip-comments` on it.

## Playbooks

Match the task to a playbook, open its file, and open a `TodoWrite` list whose first items are its steps, copied in verbatim, before any task-specific todos. A step you choose not to do stays in the list with a one-line `skip: <reason>`. When no playbook matches, say so and ask which shape the work has; do not improvise a procedure.

- **Investigate.** A read-only question: how does X work, why is Y like this, are we sure about Z. `playbooks/investigate.md`
- **Explain.** A concept, a module or a behaviour to teach by example: explain X, what does Y mean, show me how Z is used. Ends in plain words and one example, not a cited trace. `playbooks/explain.md`
- **Refactor.** Change how code is arranged without changing what it does: rename, extract, inline, group, move, dedupe, split a file. Adding or fixing behaviour has no playbook yet and is asked about. `playbooks/refactor.md`
- **Comments.** A request to strip, refactor, reduce or clean up the comments in named files. Not a playbook: apply `${CLAUDE_PLUGIN_ROOT}/skills/strip-comments/SKILL.md` with those files as the scope.

## Plan mode

Claude's plan mode and cell mode stack; plan mode wins where they disagree. In plan mode: match the playbook as usual, run its read-only steps now (reading, tests, naming the shape, the end state), and put the rest into the plan file. Each playbook that writes marks where plan mode stops. After approval, open the todo list and resume the playbook at the first step after that mark; do not redo the read-only steps. Investigate and Explain never write, so plan mode changes nothing for them.

The plan file is written for a person deciding yes or no, in this order and under eighty lines:

- **The problem.** What is hard to read or wrong today, one short paragraph, no rule recital.
- **The idea.** The end state as a story in plain words, five to ten lines, one verb per line, indented like code: no file names, no signatures, no `yield`. The shape that landed:
  ```
  checkout(order):
      look at the order
      if it is already paid:     done
      if the cart is empty:      refuse, done
      write STARTED
      charge the card            (one call, returns PAID or FAILED)
      write the result
  ```
  One block per idea. A helper the story calls does not get a second block: it gets a sentence, or a short list where every line is "question: answer". Where the callers sit is one line each after the block, not inside it. Every line of the block is "do this" or "if this: then that"; a line with no verb is a table row that wandered in.
- **What changes.** A before / after table, one row per moved or deleted thing, then the callers one line each, then the files touched as a count. More than about five files: two refactors, shown as two tables.
- **What does not change.** The promises the code keeps, and the tests that guard them, as a table of promise to test name. Count the baseline run ("31 passed"). A promise with no test is named here as the first thing to write.
- **A question, if there is one.** A behaviour choice the reshape exposes, in three lines, with the strict option named.
- **Order of work.** The playbook's remaining steps, numbered, one line each, with the break-on-purpose named per piece.
- **Verify.** The commands and what green looks like.

The reply rules below apply to the plan file too: everyday words, no `file:line` outside the tables, no paragraph where a table row will do.

## Rules

Read the leaf `SKILL.md` in full for any rule you apply. Cite only a rule whose file you opened this session, and name the specific choice it changed. Any code: name the data shape first, per **rule-typed-boundaries**, and read the language skill for the file you are in (`${CLAUDE_PLUGIN_ROOT}/skills/python/SKILL.md` for `.py`, `${CLAUDE_PLUGIN_ROOT}/skills/typescript/SKILL.md` for `.ts` and `.tsx`) for how each rule is spelled there. Each entry names when it applies, then the rule.

- **Smallest change** (**rule-smallest-change**). Any code change, sizing a diff, tempted to add a layer or a helper. The minimum code that solves the asked problem; every changed line traces to the request.
- **No pass-through** (**rule-no-pass-through**). A function whose body is one call with the same arguments. Delete it; callers call the real thing.
- **Split on the seam** (**rule-split-on-the-seam**). A file near the project's line cap, or a module with two subjects. One file, one responsibility; split where the imports divide, never raise the cap.
- **Typed boundaries** (**rule-typed-boundaries**). Data entering from outside, a signature reaching for a loose map or `any`, two components meeting. Parse into a typed model at the boundary, pass the model inside; a seam is an interface.
- **Group by subject** (**rule-group-by-subject**). Two or more functions taking the same first argument, or a class being born. They stay functions in one module named for the subject; a class is earned only by state it hides or a decision it makes.

## Reply

Write the reply clean as you draft it. It is read by a person, not graded by a machine.

- Lead with the outcome in one line: what was done, or what was decided, or the question. Who it is for and what changes for them is that line, not a heading.
- Everyday words. No fold, seam, retrofit, probe, fire, terminal, stream, yield. If a word needs the codebase to make sense, use the plain one.
- Reasons are one line each, numbered when there are more than one. Options are one line each.
- Evidence is a short parenthetical or a link, never a quoted paragraph. A rule is cited by its file and a few of its words. A number carries its source: measured, inferred, or guess. Never hand the user a check you could have run.
- Length follows the work. A decision or a small change is under fifteen lines. Only a playbook that names sections gets sections, and every one it names stays.
- What the next engineer inherits is one sentence at the end, only when there is one.
- Short declarative sentences. No em dash. A colon before a list is fine, a colon as a connector is not.
- Never invent a link, a line number, or a quote. Cite only what you read this session.
