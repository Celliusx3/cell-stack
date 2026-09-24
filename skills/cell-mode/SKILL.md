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

Match the task to a playbook, open its file, and open a `TodoWrite` list whose first items are its steps, copied in verbatim, before any task-specific todos. A step you choose not to do stays in the list with a one-line `skip: <reason>`. With no `TodoWrite` tool in the session, number the steps in your first message instead, skips included, so the person sees them. When no playbook matches, say so and ask which shape the work has; do not improvise a procedure.

- **Investigate.** A read-only question: how does X work, why is Y like this, are we sure about Z. `playbooks/investigate.md`
- **Explain.** A concept, a module or a behaviour to teach by example: explain X, what does Y mean, show me how Z is used. Ends in plain words and one example, not a cited trace. `playbooks/explain.md`
- **Refactor.** Change how code is arranged without changing what it does: rename, extract, inline, group, move, dedupe, split a file. Fixing behaviour is the Fix playbook. `playbooks/refactor.md`
- **Fix.** Behaviour that is wrong: a bug, a regression, "X returns nothing", "Y crashes", "Z is slow". Reproduce, root cause, regression test first. `playbooks/fix.md`
- **Feature.** New behaviour: add, support, allow, a new flag, endpoint, command or field. Research first, a subagent writes. `playbooks/feature.md`
- **Comments.** A request to strip, refactor, reduce or clean up the comments in named files. Not a playbook: apply `${CLAUDE_PLUGIN_ROOT}/skills/strip-comments/SKILL.md` with those files as the scope.

## Plan mode

Claude's plan mode and cell mode stack; plan mode wins where they disagree. `/research` runs during planning; the plan carries one line per decision naming who else does it, and the full table goes in the reply, never the plan. In plan mode: match the playbook as usual, run its read-only steps now (reading, tests, naming the shape, the end state), and put the rest into the plan file. Each playbook that writes marks where plan mode stops. After approval, open the todo list and resume the playbook at the first step after that mark; do not redo the read-only steps. Investigate and Explain never write, so plan mode changes nothing for them.

The plan file is written for a person deciding yes or no. Keep it simple: under fifty lines, one idea per section, and a section that runs past ten lines is cut, not explained. Lead each section with one concrete example (what the person says, what they see, what happens) before any list or table; a plan the person cannot picture is not ready. In this order:

- **What it does.** One sentence a person who never saw the code would follow: what this changes, for whom, and what it leaves alone. Then one example of the difference. With the next section, this is plan mode's Context.
- **The problem.** What is hard to read or wrong today, one short paragraph, no rule recital.
- **The idea.** For a feature: one walkthrough, numbered, of a person using it ("You say X. A card appears with Y. You tap Z, and..."). For a refactor: the end state as a story in plain words, five to ten lines, one verb per line, indented like code: no file names, no signatures, no `yield`. The shape that landed:
  ```
  checkout(order):
      look at the order
      if it is already paid:     done
      if the cart is empty:      refuse, done
      write STARTED
      charge the card            (one call, returns PAID or FAILED)
      write the result
  ```
  One block per idea. A helper the story calls does not get a second block: it gets a sentence, or a short list where every line is "question: answer". Where the callers sit is one line each after the block, not inside it. Every line of the block is "do this" or "if this: then that"; a line with no verb is a table row that wandered in. When the plan changes something the person has already met, each item is a before and after: what happened (their words, or the command and its output) and what happens next time.
- **Decisions.** One line each: the choice, and who else does it the same way. No table of sources here; that is the reply's.
- **What changes.** For a feature: the files, one line each saying what the file gains, grouped by commit. For a refactor: a before / after table, one row per moved or deleted thing, then the callers one line each, then the files touched as a count. More than about five files: two pieces, shown separately.
- **What does not change.** The promises the code keeps, and the tests that guard them, as a table of promise to test name. Count the baseline run ("31 passed"). A promise with no test is named here as the first thing to write. For a feature this may be one line: the baseline count and the test files that must stay green.
- **Later.** Things this plan deliberately leaves out, one line each, saying why nothing here changes for them.
- **A question, if there is one.** A behaviour choice the reshape exposes, in three lines, with the strict option named.
- **Order of work.** The playbook's remaining steps, numbered, one line each, with the break-on-purpose named per piece.
- **Verify.** The commands and what green looks like.

The reply rules below apply to the plan file too: everyday words, no `file:line` outside the tables, no paragraph where a table row will do.

## Autonomy

A playbook runs end to end in one turn; do not stop to ask mid-way. A "which approach" fork is settled by running the cheaper option, or by the research table, and the pick is reported as a decision with its alternatives. Pause only before an irreversible write (a commit, a push, a delete outside the working tree, a message to a person) or a genuine product call no experiment can settle. Plan mode is the one deliberate pause, at the playbook's stop line.

## Subagents

`Explore` when it must not write; `general-purpose` when it writes. The prompt is a file under the skill's `references/`, passed verbatim, followed by the scope. Parallel spawns go in one message. No `model` unless the skill says so. You own every subagent's work: read its diff, run the tests yourself, and never relay a "looks good". Read what it says it could not do before you read its diff. A subagent that reports a forced workaround has found something, and a workaround that widens the shipped code rather than the test is **rule-suspect-the-test**, not a deviation to accept. A subagent that cannot start (a usage limit, an error) is not a skipped step: do its work yourself under the same rules, and say so in the reply.

## Rules

Read the leaf `SKILL.md` in full for any rule you apply. Cite only a rule whose file you opened this session, and name the specific choice it changed. Any code: name the data shape first, per **rule-typed-boundaries**, and read the language skill for the file you are in (`${CLAUDE_PLUGIN_ROOT}/skills/python/SKILL.md` for `.py`, `${CLAUDE_PLUGIN_ROOT}/skills/typescript/SKILL.md` for `.ts` and `.tsx`) for how each rule is spelled there. Each entry names when it applies, then the rule.

- **Smallest change** (**rule-smallest-change**). Any code change, sizing a diff, tempted to add a layer or a helper. The minimum code that solves the asked problem; every changed line traces to the request.
- **No pass-through** (**rule-no-pass-through**). A function whose body is one call with the same arguments. Delete it; callers call the real thing.
- **Split on the seam** (**rule-split-on-the-seam**). A file near the project's line cap, or a module with two subjects. One file, one responsibility; split where the imports divide, never raise the cap.
- **Typed boundaries** (**rule-typed-boundaries**). Data entering from outside, a signature reaching for a loose map or `any`, two components meeting. Parse into a typed model at the boundary, pass the model inside; a seam is an interface.
- **Group by subject** (**rule-group-by-subject**). Two or more functions taking the same first argument, or a class being born. They stay functions in one module named for the subject; a class is earned only by state it hides or a decision it makes.
- **Keep logic pure** (**rule-keep-logic-pure**). A body that both talks to the outside (a file, a socket, the clock, React) and decides something. The decision is a plain function beside it, typed in and out; the shell is the read and the call.
- **Strengthen the type** (**rule-strengthen-the-type**). A throw, a null check or a "should never happen" for a case the caller cannot produce. Push the case into the parameter type and delete the check; total functions take the plain type.
- **Suspect the test** (**rule-suspect-the-test**). A test is red and the only fix is a shape you would not otherwise write, or a subagent worked around the brief in the code. Ask what the test exercises; one asserting the client, the framework or the standard library is testing someone else's code.
- **Leave generated alone** (**rule-leave-generated-alone**). A file something else writes: a vendored component, a generated client, a lockfile, a snapshot. Read it, never edit it; reach the result from outside, and know what an installer rewrites before running it.
- **Place by kind** (**rule-place-by-kind**). A new module, package or test file, or its name. It goes where the project keeps its kind, named for its subject in that folder's words; one older file elsewhere is an outlier, not a precedent.
- **Spell the call** (**rule-spell-the-call**). Text a model will follow: a skill, a tool description, a system prompt. Write each call exactly, name and arguments, and keep one worked example that a test runs.

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
- When the person says they are lost, or asks how something works, answer with one concrete example first (what they do, what they see, what happens), then the reasons. An example beats a table.
