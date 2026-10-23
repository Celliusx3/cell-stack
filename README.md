# cellstack

One front door, `/cell-mode`, on by default in every session through a hook. You type a task, and it matches the task to a playbook. It copies the playbook's steps into a todo list, and reads the project's own `CLAUDE.md` as the rules for that repo. It ends with a reply where every claim carries its evidence. The shape is [pstack](https://github.com/cursor/plugins/tree/main/pstack)'s, and every file here is written fresh.

## Install

```sh
claude --plugin-dir ~/Desktop/cellstudio/cellstack
```

`make check` validates the manifest and the structure rules. `make help` lists the rest.

## What the mode reads

`/cell-mode` is the only skill and the only command. Everything else is a plain page inside it, under `skills/cell-mode/`, that the mode reads by path when a step names it. The mode lists every procedure, so a request like "commit this" finds its page.

| Page | The mode reads it |
|---|---|
| `procedures/grill.md` | a new feature: rounds of numbered questions about what you want, each with a recommended answer |
| `procedures/research.md` | before designing: what others built, with links, and the options it leaves |
| `procedures/spec.md` | after the grill and research: the feature written down as one spec you approve |
| `procedures/tickets.md` | after the spec: one file per ticket, thinnest ticket first, each with its checks and blockers |
| `procedures/strip-comments.md` | before review: strips the comments a file does not need and fixes the code that needed them |
| `procedures/write-how-to-use.md` | a change must be shown in the real app, and the repo has no skill for it. It writes one that starts the app, uses one feature, and keeps the proof |
| `procedures/commit.md` | you asked for commits: one commit per story, each proven to pass on its own. Nothing is pushed |
| `languages/python.md`, `languages/typescript.md` | how every rule is spelled in that language. The mode reads the one for the file you are in |

Every text the mode writes for you follows its Writing section, in the spirit of ASD-STE100. A step holds one action, and each thing keeps one word. A sentence has at most 20 words in a numbered step and 25 elsewhere. `scripts/long-sentences.py` counts them, and lint runs it on every page.

Three hooks ship with the plugin. `hooks/session-start.sh` puts cell mode into context at the start of every session, so a plain request routes to a playbook without typing `/cell-mode`. `hooks/comment-nag.sh` runs after every `Edit` or `Write`. When the edit added comment lines, it tells the model to run the strip-comments procedure before handing back. `hooks/sentence-nag.sh` runs after every `Edit` or `Write` to a `.md` file in a `plans` or `specs` folder and tells the model to split long sentences.

## Adding a page

A rule is one command:

```sh
make rule name=<what-to-do>
```

A playbook, procedure or language page starts as a copy of the nearest one. [docs/adding-a-skill.md](./docs/adding-a-skill.md) is the full recipe: how to pick the kind, what to write, and what lint refuses and why.

## Status

Structure and the mode exist. Six playbooks: Investigate, Explain, Refactor, Fix, Feature, Build. Feature plans a change with you in four stages (grill, research, spec, tickets) and stops twice for you. Build then builds every ticket, committing each, and cleans up without stopping. Fifteen rules, indexed in the mode. Project rules still live in each project's `CLAUDE.md`, which the mode reads first.
