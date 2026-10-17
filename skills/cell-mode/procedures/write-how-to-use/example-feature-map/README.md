# Notes feature map

The maintained list of what a person can do in Notes, and how to prove each one works. Read this index before using the app, then follow the matching feature file.

## Before any run

- Launch Notes at `http://127.0.0.1:4173` with a throwaway data directory: `NOTES_DATA_DIR=/tmp/notes-run-$RUN_ID`, so two runs never share state.
- Seed notes titled `Quarterly plan` and `Grocery list`.
- Run `control-notes doctor` and require the expected URL, data directory and build.
- Never use a copy this run did not start.

## How to use it

- Start every recipe from the seeded state unless its preconditions say otherwise.
- Prefer ARIA roles and accessible names over CSS selectors or position.
- Browser actions go through `control-notes browser`, terminal actions through `control-notes cli -- <command>`.
- Restore the seed after a change. Never delete evidence during cleanup.

## What counts as proof

- The action and the state after it, not only the final screen.
- For a screen: an ARIA snapshot and a screenshot with the app's name visible.
- For a command: the command, stdout, stderr and the exit code.
- For a change: a second, read-only view of the stored value.
- A path that could not be reached is reported with the command tried and the missing precondition, never as verified through another path.

## The shape of a feature file

An H1, one paragraph on what the person sees, then exactly four H2s in this order:

1. `Sub-features`: short ids, one line each.
2. `How to get to it (user POV)`: every entry point.
3. `Using it with <harness>`: `Preconditions:` first, then one bullet per action pairing the exact command with what is seen.
4. `Gotchas`: what wastes or spoils a run.

Name only user paths, stable handles, required state, commands and visible proof. No implementation details.

## Features

- [Search notes](./search.md): toolbar, keyboard and CLI search, with match, empty and clear states.
