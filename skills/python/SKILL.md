---
name: python
description: How the rules are spelled in Python. Applied to any .py file; read after the rule it spells.
disable-model-invocation: true
---

# Python

Read the rule first; this is only how it is written here. One row per rule in the mode's index.

| Rule | In Python |
|---|---|
| **rule-smallest-change** | No `**kwargs` passed through "for later", no `Optional` parameter for a caller that does not exist, no `try/except Exception` around a call that cannot raise. A new module needs an importer outside `tests/`. |
| **rule-no-pass-through** | `def f(x): return g(x)` is deleted. So is a `@property` that returns a field the caller could read, a `@staticmethod` that forwards to a module function, and a `__init__.py` re-export nobody imports. A wrapper survives only when it converts, defaults, checks, or translates an exception. |
| **rule-split-on-the-seam** | The seam is the import block. A module that imports only `pydantic` or `dataclasses` and nothing from its own package is the data; a module that imports the data and a client (`httpx`, a repository, an LLM client) is the decision. Split at that line; name the new module for what it does, never `utils.py` or `helpers.py`. |
| **rule-typed-boundaries** | A typed model is a frozen Pydantic model (`model_config = ConfigDict(frozen=True)`) or `@dataclass(frozen=True)`. Parse with `Model.model_validate(raw)` at the boundary and let `ValidationError` propagate: that is failing closed. Inside, no `dict`, `dict[str, Any]`, `Any`, or `object` in a signature, and no tuple of unnamed fields (`tuple[str, str]`): a pair with known fields is a `NamedTuple` or a frozen dataclass. An interface is a `typing.Protocol`; add `@runtime_checkable` only when an `isinstance` check needs it. A genuinely open map is `dict[str, str]`. Enumerations are `Literal["a", "b"]`; a sum type is a union of models with a discriminating field. |
| **rule-group-by-subject** | The functions stay `def f(subject, ...)` in one module named for the subject. A class that is earned is a frozen dataclass or Pydantic model whose fields are what it hides (a client, a repository, a config), named subject plus role (`OrderRepository`, `MailSender`); methods are verb phrases and stay pure where the functions were pure. No one-field wrapper around a value the caller already holds, no class of `@staticmethod`s, no class with no field. |
| **rule-keep-logic-pure** | The decision is a module-level `def` that imports no framework: no `fastapi`, `httpx`, `sqlalchemy` or `asyncio` in it. The shell is the route, the CLI entry, or the `async def` that awaits the client and calls it. Tested with a plain `pytest` function that hands it values, and no fixture for the framework. |
| **rule-strengthen-the-type** | An `assert x is not None` or a `raise` for an impossible case becomes a narrower parameter. `Sequence[T]` stays where every operation is total; a `NonEmpty` is a `tuple[T, *tuple[T, ...]]` alias; a `Literal[...]` replaces a string checked against a set; `Optional` is removed from a parameter no caller passes `None` to. No `# type: ignore` and no `cast` to get past it. |

Also here: `from __future__ import annotations` at the top of every module; `logging`, never `print`, in library code; tests are `pytest` functions named for the promise they check (`test_a_failed_summary_changes_nothing`).

Examples: `references/patterns.md`.
