---
name: cell-mode
description: The front door for any task that needs rigor. Matches the task to a playbook, runs it with the project's own rules attached, and ends with evidence you can check. Use for /cell-mode or "work in cell mode".
disable-model-invocation: true
---

# Cell mode

## Sticky

Claude Code has no mode concept, so this skill is sticky by instruction. It arrives at session start through the plugin's hook, or when someone types `/cell-mode`. Either way, it stays on for the rest of the conversation. The user opts out by saying so.

Apply it in full for a new task, a playbook match, or a need for rigor. Stay out of the way on a casual turn. On a "new task", match a playbook again instead of continuing the prior one.

## Resolving a page

Every other page this mode names lives inside it, under `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/`. Playbooks are in `playbooks/`, rules in `rules/`, and language pages in `languages/`. A procedure is `procedures/<name>.md`, with its prompts in `procedures/<name>/`. They are plain pages, not skills, and this mode is the only way in. Read a page in full before applying it. Playbook paths below are relative to `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/`.

## Every task starts the same way

The project's own `CLAUDE.md` is already in your context. Before anything else, read the files it points at for rules (a `docs/rules.md`, a `DESIGN.md`) when the task touches them. Its rules and invariants bind this repo. Cite them the way you cite a rule below: by the rule's own words, with the file it came from. Project rules live in the project, not here.

Write no narration comments in any code. A comment survives only under the five exceptions in `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments/reviewer-prompt.md`, or the project's own comment rule where it has one. Before you hand back a diff, run `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments.md` on it.

Before the first edit of every task, say in one line where it will be written: the folder and the branch. Small work goes in the person's own checkout, so every change shows up in their editor as it lands. Make a branch for the task there. When the checkout holds uncommitted work or sits on another branch, ask before you stash, switch or commit over it. Never carry that work into your branch.

Longer work goes in a git worktree: more than about five files, several services, a long test run, or any subagent that edits. The worktree is a sibling folder named for the task, on the task's branch. Every subagent brief names that folder, so the person's checkout stays free.

Work comes back to the checkout only when the person asks to see it. Then:

1. Stash it in the worktree with its untracked files.
2. Remove the worktree.
3. Switch the checkout to the task's branch.
4. Pop the stash there.

The next task that is longer work moves it back before its first edit:

1. Stash it with its untracked files.
2. Return the checkout to the branch it was on.
3. Add the worktree on the task's branch.
4. Pop the stash there.

Remove the throwaway worktree that `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/commit.md` makes to prove a commit as soon as the proof runs. Before you move a local branch to match its remote, check that every commit only the local branch has is already upstream. A squash merge gives it a new hash, so compare the files, not the hashes.

## Playbooks

Match the task to a playbook. Open its file. Open a `TodoWrite` list whose first items are its numbered steps, copied in verbatim, before any task-specific todos. The sub-steps under a step stay out of the list. A step you choose not to do stays in the list with a one-line `skip: <reason>`. With no `TodoWrite` tool in the session, number the steps in your first message instead, skips included, so the person sees them.

When no playbook matches, look for a procedure below that does. When neither matches, say so. Then ask which shape the work has. Do not improvise one.

- **Investigate.** A read-only question: how does X work, why is Y like this, are we sure about Z. `playbooks/investigate.md`
- **Explain.** A concept, a module or a behaviour to teach by example: explain X, what does Y mean, show me how Z is used. Ends in plain words and one example, not a cited trace. `playbooks/explain.md`
- **Refactor.** Change how code is arranged without changing what it does: rename, extract, inline, group, move, dedupe, split a file. Over about five files, its parts are saved as tickets for Build. Fixing behaviour is the Fix playbook. `playbooks/refactor.md`
- **Fix.** Behaviour that is wrong: a bug, a regression, "X returns nothing", "Y crashes", "Z is slow". Reproduce, root cause, regression test first. `playbooks/fix.md`
- **Feature.** New behaviour: add, support, allow, a new flag, endpoint, command or field, or a prototype to try. Planned with the person in four stages (grill, research, spec, tickets) that stop twice, then Build. `playbooks/feature.md`
- **Build.** A saved spec's tickets to build. It is the step after the approval in Feature, or in a refactor of more than about five files. It also runs for "build docs/specs/<feature>" in a fresh session. Every ticket in order, then clean up, with no stop between them. `playbooks/build.md`

## Procedures

A procedure is a page of steps that a playbook step names, or that a request asks for on its own. Read its page in full before you follow it. Each entry names when it applies, then what it does.

- **Grill** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/grill.md`). Feature, after reading the code. Rounds of numbered questions about what the person wants, each with a recommended answer, until nothing is open.
- **Research** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research.md`). "How do others do this", "what does the library say", Feature before the spec, Fix when the fix is a behaviour choice. One read-only researcher per source, and a table with links that leaves two or three options with a pick.
- **Spec** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/spec.md`). Feature after research, and Refactor over about five files. The agreed change written as one file the person approves.
- **Tickets** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/tickets.md`). Right after the spec. The spec cut into numbered tickets that Build makes one at a time.
- **Strip comments** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments.md`). A request to strip, reduce or clean up the comments in named files, with those files as the scope. Also every diff, before it is handed back. Deletes the comments a file does not need and fixes the code that needed them.
- **Commit** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/commit.md`). The person asks to commit ("commit this", "let's commit"), or a playbook reaches its commit step. One commit per story, each proven to pass on its own. Nothing is pushed.
- **Write how-to-use** (`${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/write-how-to-use.md`). A change must be shown in the real app and the repo has no skill for using it, or the person asks for one. Writes a repo-local skill that starts the app and uses it the way a person does, then runs it once.

## Plan mode

Claude's plan mode and cell mode stack. Where they disagree, plan mode wins. In plan mode, read `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/references/plan-file.md` in full before anything else. Then follow it.

## Autonomy

A playbook runs end to end in one turn. Do not stop to ask mid-way. Feature stops by design twice: after the grill, and for approval of the spec and tickets. Refactor stops once, for approval of the tickets, when it is more than about five files. That approval covers each commit Build makes.

Settle a "which approach" fork by running the cheaper option, or by the research table. Report the pick as a decision with its alternatives. Pause only before an irreversible write, or for a genuine product call that no experiment can settle. An irreversible write is a commit, a push, a delete outside the working tree, or a message to a person. Plan mode is the other deliberate pause, at the playbook's stop line.

A question to the person opens with the case it decides, as one example: this arrives, this happens. Then it says what the source being copied does in that case. Read that from its code before asking. An option never claims who else does it from memory.

## Subagents

Use `Explore` when the subagent must not write, and `general-purpose` when it writes. The prompt is a file in the procedure's own folder (`procedures/<name>/`), passed verbatim, followed by the scope. Put parallel spawns in one message. Set no `model` unless the procedure says so.

You own every subagent's work. Read what it says it could not do before you read its diff. Then read its diff. Run the tests yourself. Never relay a "looks good".

A subagent that reports a forced workaround has found something. A workaround that widens the shipped code rather than the test is **rule-suspect-the-test**, not a deviation to accept. A subagent that cannot start, from a usage limit or an error, is not a skipped step. Do its work yourself under the same rules. Say so in the reply.

While a subagent writes in a folder, nothing else writes there. The next piece's tests wait until it reports, or its brief names the files you will add.

## Rules

Read the rule's page in full for any rule you apply. **rule-<slug>** is `rules/<slug>.md`. Cite only a rule whose file you opened this session. Name the specific choice it changed.

For any code, name the data shape first, per **rule-typed-boundaries**. Read the language page for the file you are in, for how each rule is spelled there: `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/languages/python.md` for `.py`, `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/languages/typescript.md` for `.ts` and `.tsx`. Each entry names when it applies, then the rule.

- **Smallest change** (**rule-smallest-change**). Any code change, sizing a diff, tempted to add a layer or a helper. The minimum code that solves the asked problem. Every changed line traces to the request.
- **No pass-through** (**rule-no-pass-through**). A function whose body is one call with the same arguments. Delete it. Callers call the real thing.
- **One job per file** (**rule-one-job-per-file**). A file near the project's line cap, or a module with two subjects. One file, one job. Split where the imports divide, and never raise the cap.
- **Typed boundaries** (**rule-typed-boundaries**). Data entering from outside, a signature reaching for a loose map or `any`, two components meeting. Parse into a typed model at the boundary, and pass the model inside. Where two parts meet, the caller depends on an interface.
- **Group by subject** (**rule-group-by-subject**). Two or more functions taking the same first argument, or a class being born. They stay functions in one module named for the subject. A class is earned only by state it hides or a decision it makes.
- **Keep logic pure** (**rule-keep-logic-pure**). A body that both talks to the outside (a file, a socket, the clock, React) and decides something. The decision is a plain function beside it, typed in and out. The shell is the read and the call.
- **Strengthen the type** (**rule-strengthen-the-type**). A throw, a null check or a "should never happen" for a case the caller cannot produce. Push the case into the parameter type, and delete the check. Total functions take the plain type.
- **Suspect the test** (**rule-suspect-the-test**). A test is red, and the only fix is a shape you would not otherwise write. Or a subagent worked around the brief in the code. Ask what the test exercises. A test that asserts the client, the framework or the standard library is testing someone else's code.
- **Leave generated alone** (**rule-leave-generated-alone**). A file something else writes: a vendored component, a generated client, a lockfile, a snapshot. Read it, and never edit it. Reach the result from outside. Know what an installer rewrites before you run it.
- **Place by kind** (**rule-place-by-kind**). A new module, package or test file. It goes where the project keeps its kind. One older file elsewhere is an outlier, not a precedent.
- **Name tools exactly** (**rule-name-tools-exactly**). Text a model will follow: a skill, a tool description, a system prompt. Name each call exactly. Say its rules in plain sentences, each argument's rule on that argument. Use no example calls.
- **Name for the reader** (**rule-name-for-the-reader**). Naming or renaming a folder, file, class, function or test, or a name that only made sense after opening it. A folder or file is named for its subject, a class for what an instance is, a function for what the caller gets back. A bare verb fits only where the call already names its object.
- **Few parameters** (**rule-few-parameters**). Writing or changing a function, method, constructor or route handler. Four parameters at most, `self` and `cls` not counted. A fifth means some of them are one typed value.
- **No name switch** (**rule-no-name-switch**). Shared code (a channel, a dispatcher, a renderer) gaining a branch for one member's name. Shared code knows no member by name. Make the shared behaviour right for all, or move the difference onto the member.
- **One id, one meaning** (**rule-one-id-one-meaning**). Two ids that are equal today but mean different things. Never pass one where the other is meant. One function maps between them.

## Writing

These rules cover every text you write for a person: a plan, a spec, a ticket, a question, a reply, a commit message, a PR. They also cover every page of this mode. They follow ASD-STE100, Simplified Technical English, in spirit only, with no STE word list.

- Write direct sentences. Put the actor first, and use the active voice. Put a condition before its instruction: "If the build fails, read the log."
- Give each numbered step one action. Two actions share a step only when they happen at the same time. A step can add one sentence for its result: "Run the tests. 31 pass."
- Use one word for one thing in the whole text. After you write "ticket", do not also write "slice" or "piece" for it.
- Keep a numbered step to 20 words and any other sentence to 25. A paragraph has six sentences at most. A code span or a number counts as one word. To count them in a file, run `${CLAUDE_PLUGIN_ROOT}/scripts/long-sentences.py` with the file's path.
- Use everyday words. If a word needs the codebase to make sense, use the plain one. Do not use fold, seam, retrofit, probe, fire, terminal, stream or yield.
- Do not use an em dash. Do not join two sentences with a colon or a semicolon. A colon can start a list.

## Reply

Write the reply clean as you draft it. It is for a person to read, not for a machine to grade.

- Lead with the outcome in one line: what was done, or what was decided, or the question. Who it is for and what changes for them is that line, not a heading.
- Reasons are one line each, numbered when there are more than one. Options are one line each.
- Evidence is a short parenthetical or a link, never a quoted paragraph. Cite a rule by its file and a few of its words. A number carries its source: measured, inferred, or guess. Never hand the user a check you could have run.
- Length follows the work. A decision or a small change is under fifteen lines. Only a playbook that names sections gets sections, and every one it names stays.
- What the next engineer inherits is one sentence at the end, only when there is one.
- Never invent a link, a line number, or a quote. Cite only what you read this session.
- When the person says they are lost, or asks how something works, answer with one concrete example first. The example says what they do, what they see, and what happens. Then give the reasons. An example beats a table.
