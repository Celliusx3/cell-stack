---
name: rule-leave-generated-alone
description: Generated and vendored files are read, never edited. Change the thing that produces them, or configure them from outside. Know what an installer rewrites before you run it. The user's decision, 2026-09-23.
disable-model-invocation: true
user-invocable: false
---

# Leave generated alone

## When

You are about to edit a file that something else writes: a component copied in by a component library's own command, a client generated from a schema, a lockfile, a migration already applied, a compiled bundle, a snapshot a test writes. Also before running any `init`, `add` or `generate` in a repo that already has hand-written files.

## Rule

Read it, do not edit it. The next regeneration silently discards what you wrote, and the bug comes back with nobody able to see why. Reach the result from outside instead: pass a setting, alias a name it already reads, wrap it, or change the source it is generated from.

Before running a generator in an existing repo, list the committed files it will rewrite and confirm they are clean, so you can revert exactly what you did not want. Keep the tool's plumbing, revert its opinions.

Instead of the tempting thing: do not make one small edit because the generated default is nearly right. Nearly right, written twice, is a file nobody trusts.

## The test

Ask who writes this file next time. If the answer is a command rather than a person, you are not allowed to be the person.
