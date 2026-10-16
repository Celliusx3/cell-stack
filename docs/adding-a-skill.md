# Adding a skill

## What a skill is

A skill is a directory under `skills/` with a `SKILL.md` in it. When you type `/<name>`, Claude Code pastes that file's body into the conversation as your message. cellstack has one skill, `cell-mode`, and it is the only thing typed. Everything else is a plain page inside it, with no frontmatter, that the mode reads by path when a step names it. That is the whole mechanism. There is no engine: a skill is a saved prompt with a name, and everything bigger in cellstack (the playbooks, rules, procedures and language pages the mode reads) is the same trick with more words.

## Pick the kind

Four kinds. Each has one shape and one place it gets wired in, so adding one never touches more than two files.

| Kind | The test | Lives at | Wired by |
|---|---|---|---|
| **procedure** | It has numbered steps and may spawn subagents: `research`, `commit`. | `skills/cell-mode/procedures/<name>.md`, prompts in `procedures/<name>/` | a playbook step that names it, if any |
| **playbook** | `/cell-mode` should route a task to it: `fix`, `feature`. | `skills/cell-mode/playbooks/<name>.md` | one row in `cell-mode`'s routing table |
| **rule** | It is a rule you would cite by name. | `skills/cell-mode/rules/<slug>.md`, cited as `rule-<slug>` | one line in `cell-mode`'s rules index |
| **language** | How every rule is spelled in one language: `python`, `typescript`. | `skills/cell-mode/languages/<language>.md` | the mode names it by file extension; lint checks it spells every rule |

If it fits none of these, it does not belong here. Write it as a note in the project's `CLAUDE.md` instead.

## The recipe

A rule is one command:

```sh
make rule name=<what-to-do>
```

It copies `templates/rule.md` to `skills/cell-mode/rules/<slug>.md`, fills in the name, appends the rule's line to the **end** of `skills/cell-mode/SKILL.md`, and runs `make lint`.

Any other kind starts as a copy of the nearest page of that kind: a playbook from `skills/cell-mode/playbooks/fix.md`, a procedure from `skills/cell-mode/procedures/research.md` and its folder, a language from `skills/cell-mode/languages/python.md`. Then:

1. Replace the copied text. For a rule, replace the placeholder text; the headings say what goes where.
2. Wire it as the kinds table says. A rule's line is already at the end of `skills/cell-mode/SKILL.md`: move it under `## Rules` and finish its sentence. A rule also needs its row in `skills/cell-mode/languages/python.md` and `skills/cell-mode/languages/typescript.md`; until then lint names both. A playbook gets its row under `## Playbooks`.
3. `make lint`.
4. `/reload-plugins` in a running session, or start one with `claude --plugin-dir ~/Desktop/cellstudio/cellstack`, and give `/cell-mode` a task that reaches it.

### What to write, per kind

**procedure.** Under `## Steps`, numbered, each naming the evidence it produces. If a step says "spawn", put the subagent's prompt in `procedures/<name>/<role>-prompt.md`, name it in the page by its full `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/...` path so lint checks it exists, and pass it verbatim; name the `subagent_type` (`Explore` when it must not write, `general-purpose` when it does). Under `## Reply`, what the reply must contain, in order. Anything deterministic (a poll, a diff, a log row) goes in `scripts/` and the step says "run it".

**playbook.** Five to fifteen numbered steps. A playbook that writes carries a **Plan mode stops here** line naming which steps run during planning and which become the plan. Step 1 is always "apply the project's `CLAUDE.md`" (it is already in context; the step opens the rule files it links). Each step names its evidence. The last line is `**Reply:**` followed by what the reply must contain. Cap is 40 lines: a playbook that needs more is two playbooks.

**rule.** `## When` (the situations, concrete enough to know when it does *not* apply), `## Rule` (one or two sentences, then what to do instead of the tempting thing), `## The test` (one question that tells whether it was kept). No example section: the rule says what the example would have shown. A rule with no source is an opinion; the line under the title says the rule and where it came from.

## What lint refuses, and why

`scripts/lint.sh` runs on every `make rule` and `make check`. It exits 1 naming the file and the rule.

| Rule | Why |
|---|---|
| `skills/` holds only `cell-mode`; its `SKILL.md` frontmatter is exactly `name`, `description`, `disable-model-invocation: true`; no other page has frontmatter | `cell-mode` is the only skill, so it is the only `/` command and the one way in. `disable-model-invocation` keeps it out of the model's Skill listing; the hook puts it in context instead. A page with frontmatter looks like a skill and is not one. |
| Every playbook has a routing row, and every row points at a real file | A playbook with no row is unreachable; a row with no file is a broken promise the model will trip on mid-task. |
| Every `${CLAUDE_PLUGIN_ROOT}/...` path a page names exists | The model follows the path as written. A page that moved is a step it cannot read, and nothing else would say so. |
| Every rule page is in the index, and every indexed rule has its page | The mode cites from the index and opens `rules/<slug>.md`. An unindexed rule is never cited; an indexed rule with no page is a file the model cannot open. |
| A procedure that says "spawn" has a prompt in `procedures/<name>/` | The prompt being a file is what makes the subagent do the same thing every time. |
| No page over 150 lines, no playbook over 40 | The body is pasted into context on every use. pstack's one 2,000-line skill is the cautionary example. |
| No em dash in any `.md` | The reply rule, applied to the skills themselves. The model copies the style it reads. |

## Conventions

- Names are kebab-case plain verbs: `strip-comments`, not `remove-the-comments`. A rule's page is `rules/<what-to-do>.md`, cited as `rule-<what-to-do>`.
- The line under a page's title says what it is for; a rule's also says where it came from.
- Long material goes in a procedure's own folder, deterministic work in `scripts/`, never in the body.
- Playbook steps say what evidence they produce, not what to think about.
- Playbook steps are in a new hire's words: "run the tests first", "move one thing", "break it on purpose". Lint refuses pstack's words (pin, characterization test, mutation, reader load, subtract).
- Nothing in a page is project-specific. Project rules live in that project's `CLAUDE.md`, which the mode reads first.
