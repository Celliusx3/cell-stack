---
name: rule-leave-generated-alone
description: Generated and vendored files are read, never edited. Change the thing that produces them, or configure them from outside. Know what an installer rewrites before you run it. The user's decision, 2026-09-23.
disable-model-invocation: true
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

## Example

A component library's `init` was run in a project with a hand built colour palette. It rewrote the stylesheet with its own flat palette, swapped the dark mode trigger, and replaced the project's typeface.

The fix was not to edit the library's components to use the project's class names, which the next `add` would have undone. The stylesheet and the layout went back to their committed state, the components stayed exactly as shipped, and one block was added to the project's own stylesheet aliasing the library's colour names onto the palette that already existed. The library is styled from outside, and updating it stays a one line command.
