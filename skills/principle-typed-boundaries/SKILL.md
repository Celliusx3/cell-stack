---
name: principle-typed-boundaries
description: Parse external data into a model at the boundary and pass the model inside; no bare dict or Any past that line. A genuine open map is dict[str, str], not a model. A seam between components is a Protocol so the caller depends on the shape, not the implementation. From pstack's type-system-discipline and boundary-discipline, and dependency inversion.
disable-model-invocation: true
---

# Typed boundaries

## When

Data enters from outside: an HTTP body, a file, a config, a model's reply, an MCP result, a subprocess line. You are writing a signature and reach for `dict`, `dict[str, Any]`, `Any`, or `object` as a parameter or return. Two components meet and one would import the other's concrete class.

## Rule

At the boundary, parse into a model (a Pydantic `BaseModel` or a frozen dataclass) and fail closed on what does not fit: raise, do not guess. Past the boundary, pass the model; a bare `dict` or `Any` inside is a boundary that was skipped. Name the data shape before writing the function that uses it. Where two components meet, the caller depends on a `Protocol` naming the methods it needs, and the concrete class satisfies it structurally; that is the seam a test doubles and a second implementation plugs into.

The exception, stated so it stays narrow: a genuinely open key-value map with no known keys (HTTP headers, environment variables, a JSON Schema object being printed) is correctly `dict[str, str]` or `dict[str, object]`, not a model with no fields.

Instead of the tempting thing: do not thread a `dict` through three functions "because it is just JSON". The third function is where the KeyError lands.

## The test

For every `dict`, `Any` and `object` in a signature: which boundary did this come through, and why was it not parsed there?

## Example

Before: `load(path) -> list[dict[str, Any]]`, and three functions downstream index `row["amount"]`, one of them wrongly as `row["amt"]`. After: a frozen `Row(date: str, amount: float, memo: str)` built inside `load`, which raises on a malformed line; the three functions take `list[Row]` and the typo is a type error, not a `KeyError` at the third call. The one map left is `headers: dict[str, str]` on the HTTP client, because header names are genuinely open.
