---
name: cell-mode
description: The front door for any task that needs rigor. Matches the task to a playbook, runs it with the project's own rules attached, and ends with evidence you can check. Use for /cell-mode or "work in cell mode".
disable-model-invocation: true
---

# Cell mode

## Sticky

Claude Code has no mode concept, so this skill is sticky by instruction. Once invoked it stays on for the rest of the conversation. A new task, a playbook match, or a need for rigor means apply it in full. A casual turn means stay out of the way. "new task" means re-match a playbook instead of continuing the prior one. The user opts out by saying so.

## Resolving a skill

Every skill in this plugin is user-invocable only, so it is not in your Skill listing. It lives at `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md`. Read that file in full before applying it. Playbook paths below are relative to `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/`.

## Every task starts the same way

The project's own `CLAUDE.md` is already in your context. Before anything else, read the files it points at for rules (a `docs/rules.md`, a `DESIGN.md`) when the task touches them. Its rules and invariants are principles for this repo. Cite them the way you cite a principle below: by the rule's own words, with the file it came from. Project rules live in the project, not here.

## Playbooks

Match the task to a playbook, open its file, and open a `TodoWrite` list whose first items are its steps, copied in verbatim, before any task-specific todos. A step you choose not to do stays in the list with a one-line `skip: <reason>`. When no playbook matches, say so and ask which shape the work has; do not improvise a procedure.

- **Investigation.** A read-only question: how does X work, why is Y like this, are we sure about Z. `playbooks/investigation.md`
- **Explain.** A concept, a module or a behaviour to teach by example: explain X, what does Y mean, show me how Z is used. Ends in plain words and one example, not a cited trace. `playbooks/explain.md`

## Principles

Cite only a principle whose file you opened this session, and name the specific choice it changed. The index is empty until the rules are written; until then the project's `CLAUDE.md` is the only source.

## Reply

Write the reply clean as you draft it.

- Say who the work is for and what changes for them before any detail of how. Then what the next engineer inherits.
- Every claim carries its evidence or its label in the same sentence: measured, inferred, or guess. Never hand the user a check you could have run.
- Short declarative sentences. No em dash. A colon before a list is fine, a colon as a connector is not.
- Terse is not an excuse to drop content. Every section the playbook's reply line names stays.
- Never invent a link, a line number, or a quote. Cite only what you read this session.
