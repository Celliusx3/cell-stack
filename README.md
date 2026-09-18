# cellstack

One front door, `/cell-mode`. You type it with a task; it matches the task to a playbook, copies the playbook's steps into a todo list, reads the project's own `CLAUDE.md` as the rules for that repo, and ends with a reply where every claim carries its evidence. The shape is [pstack](https://github.com/cursor/plugins/tree/main/pstack)'s; every file here is written fresh.

## Install

```sh
claude --plugin-dir ~/Desktop/cellstudio/cellstack
```

`make check` validates the manifest and the structure rules. `make help` lists the rest.

## Adding a skill

Four kinds (steering, procedure, playbook, principle), one command:

```sh
make new kind=steering name=shorter
```

[docs/adding-a-skill.md](./docs/adding-a-skill.md) is the full recipe: how to pick the kind, what to write, what lint refuses and why, two worked examples.

## Status

Structure and the mode exist. One playbook, Investigation. No principles yet; the project's `CLAUDE.md` is the only source of rules until they are written.
