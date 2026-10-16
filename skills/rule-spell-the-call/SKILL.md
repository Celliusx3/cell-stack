---
name: rule-spell-the-call
description: Text a model follows names every call exactly and says its rules in plain sentences, with no example calls; a tool's description says what it does, when, and what comes back, and each argument's rule sits on that argument. From a failed skill reuse on 2026-09-24, and the person's call on 2026-10-11 to keep tool descriptions simple and free of examples, after which three model failures were each fixed by one sentence.
disable-model-invocation: true
user-invocable: false
---

# Spell the call

## When

Writing or editing anything a model reads and then acts on: a tool's description and its argument schema, a skill's body, a system prompt, a template the model copies into files of its own. Not a doc written for people.

## Rule

A tool's description says what the tool does, when to call it, and what comes back, in plain sentences. Each argument's rule (the characters it may hold, when to leave it out) goes in that argument's own description in the schema, where the model reads it beside the field. Text that tells the model to call another tool names it exactly, with its real name and argument names, never "use the X tool": a step that names no call leaves the model guessing a name, and the name is what it invents.

When a model gets it wrong, the fix is one plain sentence where the model reads it, recorded in the project's prompt ledger, with a test that fails if the sentence goes.

Instead of the tempting thing: do not paste an example call into a description to steer the model. It costs every request, goes stale, and the model copies its values. Say the rule the example was showing.

## The test

Read the text as the model will. Could it tell when to call each tool, what every argument must be, and what it gets back, without guessing a name? Is each argument's rule readable on its field alone?
