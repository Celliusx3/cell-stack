# cellstack

One front door, `/cell-mode`, on by default in every session through a hook. You type a task; it matches the task to a playbook, copies the playbook's steps into a todo list, reads the project's own `CLAUDE.md` as the rules for that repo, and ends with a reply where every claim carries its evidence. The shape is [pstack](https://github.com/cursor/plugins/tree/main/pstack)'s; every file here is written fresh.

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
| `procedures/tickets.md` | after the spec: one file per ticket, thinnest slice first, each with its checks and blockers |
| `procedures/strip-comments.md` | before review: strips the comments a file does not need and fixes the code that needed them |
| `procedures/write-how-to-use.md` | a change must be shown in the real app and the repo has no skill for it: writes one that starts the app, uses one feature, and keeps the proof |
| `procedures/commit.md` | you asked for commits: one commit per story, each proven to pass on its own; nothing pushed |
| `languages/python.md`, `languages/typescript.md` | how every rule is spelled in that language; the mode reads the one for the file you are in |

Two hooks ship with the plugin. `hooks/session-start.sh` puts cell mode into context at the start of every session, so a plain request routes to a playbook without typing `/cell-mode`. `hooks/comment-nag.sh` runs after every `Edit` or `Write` and, when the edit added comment lines, tells the model to run the strip-comments procedure before handing back.

## Adding a page

A rule is one command:

```sh
make rule name=<what-to-do>
```

A playbook, procedure or language page starts as a copy of the nearest one. [docs/adding-a-skill.md](./docs/adding-a-skill.md) is the full recipe: how to pick the kind, what to write, and what lint refuses and why.

## Status

Structure and the mode exist. Six playbooks: Investigate, Explain, Refactor, Fix, Feature, Build. Feature plans a change with you in four stages (grill, research, spec, tickets) and stops twice for you; Build then builds every ticket, committing each, and cleans up without stopping. Fifteen rules, indexed in the mode. Project rules still live in each project's `CLAUDE.md`, which the mode reads first.
