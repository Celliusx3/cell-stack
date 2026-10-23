# Name tools exactly

Text a model follows names every call exactly and says its rules in plain sentences, with no example calls. A tool's description says what it does, when, and what comes back. Each argument's rule sits on that argument. From a failed skill reuse on 2026-09-24. Also from the person's call on 2026-10-11 to keep tool descriptions simple and free of examples, after which one sentence each fixed three model failures.

## When

Writing or editing anything a model reads and then acts on:

- a tool's description and its argument schema
- a skill's body
- a system prompt
- a template the model copies into files of its own

It does not apply to a doc written for people.

## Rule

A tool's description says what the tool does, when to call it, and what comes back, in plain sentences. Each argument's rule goes in that argument's own description in the schema, where the model reads it beside the field. An argument's rule is the characters it may hold, and when to leave it out. Text that tells the model to call another tool names it exactly, with its real name and argument names, never "use the X tool". A step that names no call leaves the model guessing a name, and the name is what it invents.

When a model gets it wrong, the fix is one plain sentence where the model reads it. Record it in the project's prompt ledger, with a test that fails if the sentence goes.

Instead of the tempting thing, do not paste an example call into a description to steer the model. It costs every request, goes stale, and the model copies its values. Say the rule the example was showing.

## The test

Read the text as the model will. Could it tell when to call each tool, what every argument must be, and what it gets back, without guessing a name? Is each argument's rule readable on its field alone?
