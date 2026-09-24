---
name: rule-place-by-kind
description: A new module goes where the project keeps its kind, named for its subject in that folder's words; one older file of the same kind elsewhere is an outlier, not a precedent. From a correction, 2026-09-24, when model tools placed beside an outlier were moved in with the other tools.
disable-model-invocation: true
---

# Place by kind

## When

Creating a module, a package or a test file, or naming one. Deciding where a new piece lives when the nearest similar file sits somewhere unusual. It does not apply to moving existing code for its own sake; that is a refactor with its own reason.

## Rule

Put new code where the project keeps things of its kind: the layout in its rules file, the path a plan names, the folder where most of its siblings live. Tools go with tools, services with services, a test beside the tests for that folder. Name it for its subject in that folder's words, never a verb joined to a layer (`edit_tools`, `skill_helpers`). One older file of the same kind somewhere else is an outlier, not a precedent. Leaving a path a plan names is a decision to raise before building, not one to take and report.

Instead of the tempting thing: do not put it beside the one similar file you happened to read first.

## The test

Cover the file name and point at its folder. Would someone who knows the layout look for it there? If they would look where its siblings live, it goes there.

## Example

Three model tools that save, delete and add files to a skill were written as `skills/edit_tools.py`, beside the one older tool that lived outside the tools folder, although the plan named `tools/native/skills/`. The person asked twice: "the naming sucks", then "it is more like function in skills service, then tool in native tool will call these skills functions". They moved to `tools/native/skills/tools.py`, next to every other tool, calling the service's own `save`, `delete` and `write_file`; the skills package kept only skill logic.
