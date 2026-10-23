# Leave generated alone

Generated and vendored files are read, never edited. Change the thing that produces them, or configure them from outside. Know what an installer rewrites before you run it. The user's decision, 2026-09-23.

## When

You are about to edit a file that something else writes:

- a component copied in by a component library's own command
- a client generated from a schema
- a lockfile, or a migration already applied
- a compiled bundle, or a snapshot a test writes

It also applies before you run any `init`, `add` or `generate` in a repo that already has hand-written files.

## Rule

Read it, and do not edit it. The next regeneration silently discards what you wrote, and the bug comes back with nobody able to see why. Reach the result from outside instead: pass a setting, alias a name it already reads, wrap it, or change the source it is generated from.

Before you run a generator in an existing repo, list the committed files it will rewrite. Confirm they are clean, so you can revert exactly what you did not want. Keep the tool's plumbing, and revert its opinions.

Instead of the tempting thing, do not make one small edit because the generated default is nearly right. Nearly right, written twice, is a file nobody trusts.

## The test

Ask who writes this file next time. If the answer is a command rather than a person, you are not allowed to be the person.
