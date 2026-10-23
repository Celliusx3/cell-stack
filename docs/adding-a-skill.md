# Adding a skill

## What a skill is

A skill is a directory under `skills/` with a `SKILL.md` in it. When you type `/<name>`, Claude Code pastes that file's body into the conversation as your message. cellstack has one skill, `cell-mode`, and it is the only thing typed. Everything else is a plain page inside it, with no frontmatter, that the mode reads by path when a step names it. That is the whole mechanism.

There is no engine. A skill is a saved prompt with a name. Everything bigger in cellstack is the same trick with more words: the playbooks, rules, procedures and language pages the mode reads.

## Pick the kind

Four kinds. Each has one shape and one place it gets wired in, so adding one never touches more than two files.

| Kind | The test | Lives at | Wired by |
|---|---|---|---|
| **procedure** | It has numbered steps and may spawn subagents: `research`, `commit`. | `skills/cell-mode/procedures/<name>.md`, prompts in `procedures/<name>/` | one line in `cell-mode`'s procedures list. A playbook step names it by its full path |
| **playbook** | `/cell-mode` should route a task to it: `fix`, `feature`. | `skills/cell-mode/playbooks/<name>.md` | one row in `cell-mode`'s routing table |
| **rule** | It is a rule you would cite by name. | `skills/cell-mode/rules/<slug>.md`, cited as `rule-<slug>` | one line in `cell-mode`'s rules index |
| **language** | How every rule is spelled in one language: `python`, `typescript`. | `skills/cell-mode/languages/<language>.md` | the mode names it by file extension. Lint checks it spells every rule |

If it fits none of these, it does not belong here. Write it as a note in the project's `CLAUDE.md` instead.

## The recipe

A rule is one command:

```sh
make rule name=<what-to-do>
```

It copies `templates/rule.md` to `skills/cell-mode/rules/<slug>.md`, and fills in the name. It appends the rule's line to the **end** of `skills/cell-mode/SKILL.md`, and runs `make lint`.

Any other kind starts as a copy of the nearest page of that kind:

- a playbook from `skills/cell-mode/playbooks/fix.md`
- a procedure from `skills/cell-mode/procedures/research.md` and its folder
- a language from `skills/cell-mode/languages/python.md`

Then:

1. Replace the copied text. For a rule, the headings say what goes where.
2. Wire it as the kinds table says.
   1. A rule's line is already at the end of `skills/cell-mode/SKILL.md`. Move it under `## Rules`, and finish its sentence.
   2. Add the rule's entry to `skills/cell-mode/languages/python.md` and `skills/cell-mode/languages/typescript.md`. Until then, lint names both.
   3. Give a playbook its row under `## Playbooks`, and a procedure its line under `## Procedures`.
3. Run `make lint`.
4. Run `/reload-plugins` in a running session, or start one with `claude --plugin-dir ~/Desktop/cellstudio/cellstack`.
5. Give `/cell-mode` a task that reaches the new page.

### What to write, per kind

Every page follows the Writing section of the mode, like any text for a person. A step holds one action, and each thing keeps one word. A sentence has at most 20 words in a numbered step and 25 elsewhere. Lint runs `scripts/long-sentences.py` on every page.

**procedure.** One line under the title says what it makes and for whom. When it runs goes in the mode's list, not the page. Under `## Steps`, write numbered steps, each naming the evidence it produces, with one-action sub-steps under them. Under `## Reply`, write what the reply must contain, in order. Anything deterministic (a poll, a diff, a log row) goes in `scripts/`, and the step says "run it".

If a step says "spawn", put the subagent's prompt in `procedures/<name>/<role>-prompt.md`. Name it in the page by its full `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/...` path, so lint checks it exists. Pass it verbatim. Name the `subagent_type`: `Explore` when it must not write, `general-purpose` when it does. There is no `## Subagents` section. The step says all of that, and the mode's Subagents section says the rest.

**playbook.** Five to fifteen numbered steps, each one short instruction. The one-action sub-steps go under each step as a nested numbered list, and only the numbered steps go into the todo list. A playbook that writes carries a **Plan mode stops here** line, naming which steps run during planning and which become the plan. Step 1 is always "apply the project's `CLAUDE.md`". It is already in context, and the step opens the rule files it links.

Each step names its evidence. The page ends with `**Reply:**` and a list of what the reply must contain. The cap is 950 words. A playbook that needs more is two playbooks.

**rule.** Three sections:

- `## When`: the situations, concrete enough to know when it does *not* apply.
- `## Rule`: one or two sentences, then what to do instead of the tempting thing.
- `## The test`: one question that tells whether it was kept.

No example section. The rule says what the example would have shown. A rule with no source is an opinion. The line under the title says the rule and where it came from.

**language.** One entry per rule in the mode's index: the rule's bold name, then short bullets on how it is spelled in that language.

## What lint refuses, and why

`scripts/lint.sh` runs on every `make rule` and `make check`. It exits 1, naming the file and the rule.

| Rule | Why |
|---|---|
| `skills/` holds only `cell-mode`. Its `SKILL.md` frontmatter is exactly `name`, `description`, `disable-model-invocation: true`. No other page has frontmatter | `cell-mode` is the only skill, so it is the only `/` command and the one way in. `disable-model-invocation` keeps it out of the model's Skill listing. The hook puts it in context instead. A page with frontmatter looks like a skill and is not one. |
| Every playbook has a routing row, and every row points at a real file | A playbook with no row is unreachable. A row with no file is a broken promise the model will trip on mid-task. |
| Every procedure page has a line in the mode's procedures list | The mode is the only text the model always sees. A procedure no line points at is reached only when a step happens to name it, and a request like "commit this" never finds it. |
| No page or hook names a slash command but `/cell-mode` | `cell-mode` is the only command. A page that names a command that does not exist leaves the model guessing a path, per `rule-name-tools-exactly`. Name the page by its path instead. |
| Every `${CLAUDE_PLUGIN_ROOT}/...` path a page names exists | The model follows the path as written. A page that moved is a step it cannot read, and nothing else would say so. |
| Every rule page is in the index, and every rule a page cites has its page | The mode cites from the index and opens `rules/<slug>.md`. An unindexed rule is never cited. A cited rule with no page, say after a rename, is a file the model cannot open. |
| A procedure that says "spawn" has a prompt in `procedures/<name>/` | The prompt being a file is what makes the subagent do the same thing every time. |
| No playbook over 950 words or outside 5 to 15 numbered steps, no `SKILL.md` over 2,700 words, no other page over 1,100 words | The body is pasted into context on every use. Words are what fills the context, so the caps count words, and a list marker is not a word. pstack's one 2,000-line skill is the cautionary example. |
| No em dash in any `.md` | The Writing rule, applied to the pages themselves. The model copies the style it reads. |
| Every page under `skills/` and `templates/`, this guide and the README keep the Writing caps of the mode (`scripts/long-sentences.py`) | The model copies the style it reads. |

## Conventions

- Names are kebab-case and follow `rule-name-for-the-reader`. Read aloud, the path says what is inside (`procedures/strip-comments.md`, `procedures/write-how-to-use.md`). A rule's page is `rules/<what-to-do>.md`, cited as `rule-<what-to-do>`.
- The line under a page's title says what it is for. A rule's line also says where it came from.
- Long material goes in a procedure's own folder, and deterministic work in `scripts/`, never in the body.
- Playbook steps say what evidence they produce, not what to think about.
- Playbook steps are in a new hire's words: "run the tests first", "move one thing", "break it on purpose". Lint refuses pstack's words (pin, characterization test, mutation, reader load, subtract).
- Nothing in a page is project-specific. Project rules live in that project's `CLAUDE.md`, which the mode reads first.
