# Name what it returns

A function's name says what the caller gets back. A yes or no reads as a question, a value is named for the value, and an action is the plain verb for what it does. From a correction on 2026-09-24, when a service's `due`, `refusal` and `reduce` became a question, a reason and a plain verb.

## When

Naming or renaming a function, a method or a helper, or reading a call site that only makes sense after you read the docstring. The signals: a bare adjective (`due`, `ready`), a bare noun that hides what comes back (`refusal`, `render`), or a verb that fits anything (`handle`, `process`, `reduce`, `do`, `manage`). It does not apply to modules and classes, which are named for their subject (**rule-place-by-kind**, **rule-group-by-subject**).

## Rule

Name each function for what the caller gets back:

1. A yes or no reads as a question: `should_close`, `is_empty`, `has_access`.
2. A value is named for the value, and adds its kind when the type does not show it: `refusal_reason`, `unposted_ids`, `timeout_seconds`.
3. An action is the plain verb for what it does, the word the person would use: `close`, `send`, `save`.

Instead of the tempting thing: do not keep a short name and explain it in the docstring. If the docstring is what makes the call readable, the docstring's words belong in the name.

## The test

Read the call site out loud without looking at the definition. `if ledger.should_close(month): ledger.close(month)` reads as a sentence. `if ledger.due(month): ledger.reduce(month)` needs the docstring. If it needs the docstring, rename it.
