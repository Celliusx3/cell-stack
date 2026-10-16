# cellstack

One front door, `/cell-mode`, on by default in every session through a hook. You type a task; it matches the task to a playbook, copies the playbook's steps into a todo list, reads the project's own `CLAUDE.md` as the rules for that repo, and ends with a reply where every claim carries its evidence. The shape is [pstack](https://github.com/cursor/plugins/tree/main/pstack)'s; every file here is written fresh.

## Install

```sh
claude --plugin-dir ~/Desktop/cellstudio/cellstack
```

`make check` validates the manifest and the structure rules. `make help` lists the rest.

## Skills

`/cell-mode` is the only command. Every other skill is hidden from the `/` menu, and the mode reads it by path when a step names it.

| Skill | The mode reads it |
|---|---|
| `research` | before designing: what others built, with links, and the options it leaves |
| `strip-comments` | before review: strips the comments a file does not need and fixes the code that needed them |
| `drive` | before a Verify step: writes the repo-local skill that starts the app, drives one feature, and keeps the proof |
| `commit` | you asked for commits: one commit per story, each proven to pass on its own; nothing pushed |
| `python`, `typescript` | how every rule is spelled in that language; the mode reads the one for the file you are in |

Two hooks ship with the plugin. `hooks/session-start.sh` puts cell mode into context at the start of every session, so a plain request routes to a playbook without typing `/cell-mode`. `hooks/comment-nag.sh` runs after every `Edit` or `Write` and, when the edit added comment lines, tells the model to run `/strip-comments` before handing back.

## Adding a skill

A rule is one command:

```sh
make rule name=<what-to-do>
```

A playbook, procedure or language page starts as a copy of the nearest one. [docs/adding-a-skill.md](./docs/adding-a-skill.md) is the full recipe: how to pick the kind, what to write, and what lint refuses and why.

## Status

Structure and the mode exist. Five playbooks: Investigate, Explain, Refactor, Fix, Feature. Feature runs its three stages in one go, with no stop for approval in between: make it work, Refactor on its diff, then Clean up. Fifteen rules, indexed in the mode. Project rules still live in each project's `CLAUDE.md`, which the mode reads first.
