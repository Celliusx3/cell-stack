---
name: rule-no-pass-through
description: A function whose whole body is one call to another callable, arguments passed straight through, is deleted and its callers call the real thing. A wrapper is earned only when it changes the arguments, the return, or the error. The user's decision, 2026-09-19.
disable-model-invocation: true
---

# No pass-through

## When

You are writing or reading a function or method whose body is a single `return other(...)` or `await other(...)` with the same arguments in the same order. Also a class method that only forwards to a module function, or a module function that only forwards to a method. It does not apply to a wrapper that renames for an interface it must satisfy (one the caller depends on), or one that adds a default, a conversion, a check, or an error translation.

## Rule

Delete the pass-through and make every caller call the real thing. Do this on sight when you touch the file, and never write a new one. If the name of the wrapper was carrying meaning, move that meaning into the name of the real thing.

Instead of the tempting thing: do not keep it "for readability" or "in case it changes later". A name with no behaviour is one more thing to read and one more place to update.

## The test

Cover the body with your hand. If the signature alone tells you what happens, and the body adds nothing to it, the function is a pass-through.

## Example

Before, a made-up two-liner in the shape this bans:

```python
def read_ledger(path: Path) -> list[Row]:
    return load(path)
```

After: `read_ledger` is gone, its callers call `load(path)`. If the file has a `load_ledger` and a `load`, one of the two names was wrong; fix the name, not the call chain.
