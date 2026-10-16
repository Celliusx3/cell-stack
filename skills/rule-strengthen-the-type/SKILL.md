---
name: rule-strengthen-the-type
description: A throw, an assert, a null check or a "should never happen" for a case the caller cannot produce marks a type that is too weak; push the case into the parameter type, delete the check, then stop. A total function takes the plain type. From pstack's type-system-discipline.
disable-model-invocation: true
user-invocable: false
---

# Strengthen the type

## When

A function body has a throw, an assert, a null check, or a comment saying "should never happen", for a case the caller cannot actually produce. Or a signature takes a loose type and then guards it: a list it refuses when empty, a string it checks against a set, an optional it rejects when missing. It does not apply at a boundary, where the data is still untyped and the check is the parse.

## Rule

Push the case into the parameter type and delete the check. Then stop: the type's job is to track the cases each call site must handle, not to describe the data as precisely as possible. Prefer total functions. pstack's own pair: `sum` of an empty list is 0, so it takes the plain list; `head` of an empty list has no answer, so it demands the non-empty one.

Instead of the tempting thing: do not add a second guard one level up, and do not brand or narrow a type where no check was ever needed. A type that was never going to fail a check is precision with no case behind it.

## The test

Which call site can pass the value this check refuses? If none, the check is a type that was not written.
