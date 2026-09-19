---
name: principle-group-by-subject
description: Two or more functions that take the same subject as their first argument become methods on one class named for that subject, which holds the argument. A lone function with one caller and no sibling stays a function. The user's decision, 2026-09-19, and a deliberate departure from pstack's minimize-reader-load, which prefers pure functions.
disable-model-invocation: true
---

# Group by subject

## When

A module has two or more functions whose first parameter is the same thing (the same events list, the same session, the same config) or that read the same module-level state. You are about to add a function that takes that same subject. It does not apply to a single function with one caller and no sibling, to a pure conversion between two types, or to a `Protocol` method.

## Rule

Give the subject a class named for it, hold the subject as its one field, and make the functions its methods. The caller then writes `subject.question()` instead of `question(subject)`, and the module reads as one thing with several questions on it rather than several functions that happen to agree on an argument. A new function on that subject is a new method; do not add a sixth free function beside five.

This is a departure, chosen on purpose: pstack's minimize-reader-load prefers pure functions and "locals over fields". The user chose grouping, so that a module's shape shows its subject. Keep the methods pure where they were pure: a method that returns an answer and mutates nothing is still that.

Instead of the tempting thing: do not create a class with no field, or one that is only a namespace for static methods. If there is no subject to hold, there is nothing to group.

## The test

Cover the function names. If the first parameters are the same word, they are one class.

## Example

Before: `total(rows)`, `by_month(rows)`, `largest(rows)` as three module functions, and a request to add `smallest(rows)`. After: `class Ledger` with one field, `rows`, and four methods; the caller writes `ledger.total()` and the module reads as one subject with four questions. `load(path) -> Ledger` is the one function left, because it is the conversion that makes the subject.
