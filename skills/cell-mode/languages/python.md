# Python

How the rules are spelled in Python. It applies to any .py file. Read it after the rule it spells.

Read the rule first. This page is only how the rule is written here. It has one entry per rule in the mode's index.

**rule-smallest-change**

- No `**kwargs` passed through "for later".
- No `Optional` parameter for a caller that does not exist.
- No `try/except Exception` around a call that cannot raise.
- A new module needs an importer outside `tests/`.

**rule-no-pass-through**

- `def f(x): return g(x)` is deleted.
- So is a `@property` that returns a field the caller could read.
- So is a `@staticmethod` that forwards to a module function.
- So is a `__init__.py` re-export nobody imports.
- A wrapper survives only when it converts, defaults, checks, or translates an exception.

**rule-one-job-per-file**

- Split at the import block.
- A module that imports only `pydantic` or `dataclasses`, and nothing from its own package, is the data.
- A module that imports the data and a client (`httpx`, a repository, an LLM client) is the code that acts on it. Its logic splits off again per **rule-keep-logic-pure**.
- The new module is named per **rule-name-for-the-reader**.

**rule-typed-boundaries**

- A typed model is a frozen Pydantic model (`model_config = ConfigDict(frozen=True)`) or `@dataclass(frozen=True)`.
- Parse with `Model.model_validate(raw)` at the boundary, and let `ValidationError` propagate. That is failing closed.
- Inside, no `dict`, `dict[str, Any]`, `Any`, or `object` goes in a signature.
- No tuple of unnamed fields (`tuple[str, str]`) goes there either. A pair with known fields is a `NamedTuple` or a frozen dataclass.
- An interface is a `typing.Protocol`. Add `@runtime_checkable` only when an `isinstance` check needs it.
- A genuinely open map is `dict[str, str]`.
- Enumerations are `Literal["a", "b"]`. A sum type is a union of models with a discriminating field.

**rule-group-by-subject**

- The functions stay `def f(subject, ...)` in one module named for the subject.
- A class that is earned is a frozen dataclass or Pydantic model whose fields are what it hides: a client, a repository, a config.
- It and its methods are named per **rule-name-for-the-reader**. The methods stay pure where the functions were pure.
- No one-field wrapper around a value the caller already holds.
- No class of `@staticmethod`s, and no class with no field.

**rule-keep-logic-pure**

- The decision is a module-level `def` that imports no framework: no `fastapi`, `httpx`, `sqlalchemy` or `asyncio` in it.
- The shell is the route, the CLI entry, or the `async def` that awaits the client and calls it.
- Test the decision with a plain `pytest` function that hands it values, and no fixture for the framework.

**rule-strengthen-the-type**

- An `assert x is not None` or a `raise` for an impossible case becomes a narrower parameter.
- `Sequence[T]` stays where every operation is total.
- A `NonEmpty` is a `tuple[T, *tuple[T, ...]]` alias.
- A `Literal[...]` replaces a string checked against a set.
- `Optional` is removed from a parameter no caller passes `None` to.
- No `# type: ignore` and no `cast` to get past it.

**rule-suspect-the-test**

- A `pytest` failure whose only fix widens a route pattern, loosens a signature, or adds a branch for an unreachable case.
- Run the client by hand first. `httpx` and `urllib` both normalise a URL before sending, `Path` collapses `.`, and `json.dumps` reorders nothing.
- A test asserting any of those is testing the library.

**rule-leave-generated-alone**

- `uv.lock`, `poetry.lock`, an applied Alembic migration, a `_pb2.py`, an OpenAPI client, a `__snapshot__`.
- Change `pyproject.toml` and re-lock, write a new migration, or edit the `.proto` or the spec.
- No hand edit, and no `# noqa` added inside a generated file.

**rule-place-by-kind**

- A new module goes in the package that holds its kind, beside its siblings (`tools/<name>/`, `services/`).
- It is exported from that package's `__init__.py`.

**rule-name-tools-exactly**

- A tool description in a `.py` file says what the tool does, when, and what comes back, with no example call.
- Each argument's rule is that field's `Field(description=...)`, which lands in the JSON schema the model reads.
- A skill body names each call with its real tool and argument names.
- A wording that fixes a model failure gets a `pytest` test asserting the sentence is in the description or the field.

**rule-few-parameters**

- Count every parameter but `self` and `cls`, keyword-only ones included.
- A FastAPI handler's path, body and dependency parameters count too.
- A fifth becomes a frozen dataclass or Pydantic model the callers build, or the object the values came from.
- Ruff's `PLR0913` with `max-args = 4` enforces it where the project turns it on.

**rule-no-name-switch**

- No `if x.name == ...` or `match` case on one member's name in a module that serves every member.
- The difference becomes a field on the member's declaration (a dataclass field, a `Protocol` method), or an entry in the registry it is built into.

**rule-one-id-one-meaning**

- Each parameter and field is named for the id it means (`bot_id`, `chat_id`).
- One method on the service that owns the relation maps between them.
- Use a `typing.NewType` per id when the type checker should catch a swap.

**rule-name-for-the-reader**

- Packages and modules are short `snake_case` nouns, classes `PascalCase`, functions `snake_case`.
- A yes or no returns `bool` and starts with `is_`, `has_`, `should_` or `can_`.
- A value is a noun phrase with no `get_` prefix (`refusal_reason`, `unposted_ids`).
- A function that returns `X | None` is named for the `X`, not for the check.
- An action is a verb and its object (`send_invoice`).
- A bare verb (`save`, `close`) fits only where the call names the object: a method, or a module function its callers write as `ledger.close(month)`.
- `from ledger import close` drops the module at the call.
- A test is a `pytest` function named for the promise it checks (`test_a_failed_summary_changes_nothing`).
- `__init__.py`, `__main__.py` and `conftest.py` keep their names.
- A Pydantic model a tool takes keeps its class name and its docstring. They are the schema's `title` and `description`. Renaming one, or editing its docstring, changes what the model reads (**rule-name-tools-exactly**).

Also, put `from __future__ import annotations` at the top of every module. Use `logging`, never `print`, in library code.
