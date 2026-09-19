# Adding a skill

## What a skill is

A skill is a directory under `skills/` with a `SKILL.md` in it. When you type `/<name>`, Claude Code pastes that file's body into the conversation as your message. That is the whole mechanism. There is no engine: a skill is a saved prompt with a name, and everything bigger in cellstack (the mode, the playbooks it routes to) is the same trick with more words.

## Pick the kind

Five kinds. Each has one shape and one place it gets wired in, so adding one never touches more than two files.

| Kind | The test | Lives at | Wired by |
|---|---|---|---|
| **steering** | You would type it to steer a reply: `/shorter`, `/plain`. | `skills/<name>/SKILL.md` | nothing. You type it. |
| **procedure** | It has numbered steps and may spawn subagents: a `/trace`, a `/compare`. | `skills/<name>/SKILL.md` + `references/` | a playbook step that names it, if any |
| **playbook** | `/cell-mode` should route a task to it: `bug-fix`, `phase`. | `skills/cell-mode/playbooks/<name>.md` | one row in `cell-mode`'s routing table |
| **rule** | It is a rule you would cite by name. | `skills/rule-<slug>/SKILL.md` | one line in `cell-mode`'s rules index |
| **language** | How every rule is spelled in one language: `python`, `typescript`. | `skills/<language>/SKILL.md` + `references/patterns.md` | the mode names it by file extension; lint checks it spells every rule |

If it fits none of these, it is not a skill. Write it as a note in the project's `CLAUDE.md` instead.

## The recipe

One command for every kind:

```sh
make new kind=<steering|procedure|playbook|rule> name=<kebab-case>
```

It copies the kind's template from `templates/`, fills in the name, adds the wiring line where the kind needs one, and runs `make lint`. Then:

1. Open the file it created and replace the placeholder text. The template's headings say what goes where.
2. For a playbook or rule, the wiring line was appended to the **end** of `skills/cell-mode/SKILL.md`. Move it under `## Playbooks` or `## Rules` and finish its sentence.
3. `make lint`.
4. `/reload-plugins` in a running session, or start one with `claude --plugin-dir ~/Desktop/cellstudio/cellstack`, and type `/<name>`.

### What to write, per kind

**steering.** One to five sentences. Say what to do with the last message or with the text after the command. No steps, no headings. `/bro` in pstack is two sentences and earns its place.

**procedure.** Under `## Steps`, numbered, each naming the evidence it produces. If a step says "spawn", put the subagent's prompt in `references/<role>-prompt.md` and pass it verbatim; name the `subagent_type` (`Explore` when it must not write, `general-purpose` when it does). Under `## Reply`, what the reply must contain, in order. Anything deterministic (a poll, a diff, a log row) goes in `scripts/` and the step says "run it".

**playbook.** Five to fifteen numbered steps. A playbook that writes carries a **Plan mode stops here** line naming which steps run during planning and which become the plan. Step 1 is always "apply the project's `CLAUDE.md`" (it is already in context; the step opens the rule files it links). Each step names its evidence. The last line is `**Reply:**` followed by what the reply must contain. Cap is 40 lines: a playbook that needs more is two playbooks.

**rule.** `## When` (the situations, concrete enough to know when it does *not* apply), `## Rule` (one or two sentences, then what to do instead of the tempting thing), `## Example` (one from your own code or a past correction, with a path). A rule with no source is an opinion; write where it came from in the description.

## What lint refuses, and why

`scripts/lint.sh` runs on every `make new` and `make check`. It exits 1 naming the file and the rule.

| Rule | Why |
|---|---|
| Frontmatter is exactly `name`, `description`, `disable-model-invocation: true`; `name` equals the directory | The three fields are all Claude Code reads. `disable-model-invocation` keeps every skill user-triggered, so the model reaches them by path, never by guessing. A mismatched name is a `/command` that does not exist. |
| Every playbook has a routing row, and every row points at a real file | A playbook with no row is unreachable; a row with no file is a broken promise the model will trip on mid-task. |
| Every `rule-*` is in the index | The mode cites from the index. An unindexed rule is never cited. |
| A procedure that says "spawn" has a `references/` prompt | The prompt being a file is what makes the subagent do the same thing every time. |
| No `SKILL.md` over 150 lines, no playbook over 40 | The body is pasted into context on every use. pstack's one 2,000-line skill is the cautionary example. |
| No em dash in any `.md` | The reply rule, applied to the skills themselves. The model copies the style it reads. |

## Conventions

- Names are kebab-case and read as a command: `/shorter`, not `/make-it-shorter`.
- The `description` is the phrasings that should trigger it. It is the only text the `/` menu shows.
- Long material goes in `references/`, deterministic work in `scripts/`, never in the body.
- Playbook steps say what evidence they produce, not what to think about.
- Playbook steps are in a new hire's words: "run the tests first", "move one thing", "break it on purpose". Lint refuses pstack's words (pin, characterization test, mutation, reader load, subtract).
- Names are plain verbs: `/explain`, `/refactor`, `/strip-comments`. A rule is `rule-<what-to-do>`.
- Nothing in a skill is project-specific. Project rules live in that project's `CLAUDE.md`, which the mode reads first.

## Worked examples

### A steering skill: `/shorter`

```sh
make new kind=steering name=shorter
```

Edit `skills/shorter/SKILL.md`:

```markdown
---
name: shorter
description: Restate the last message in half the words. Use for /shorter or "too long".
disable-model-invocation: true
---

Restate your last message in at most half the words. Keep every claim and its evidence. Drop the framing, the hedges, and anything the reader already knows.
```

`make lint`, then `/shorter` after any reply.

### A playbook: `bug-fix`

```sh
make new kind=playbook name=bug-fix
```

Edit `skills/cell-mode/playbooks/bug-fix.md` (steps: read `CLAUDE.md`; reproduce first and paste the failing output; find the cause with evidence; smallest fix; rerun the repro; propose the commit). Then in `skills/cell-mode/SKILL.md`, move the appended line under `## Playbooks` and finish it:

```markdown
- **Bug fix.** A reported defect to reproduce, root-cause and fix with the repro rerun. `playbooks/bug-fix.md`
```

`make lint` checks the row and the file agree. From then on `/cell-mode the export writes duplicate rows` routes there.
