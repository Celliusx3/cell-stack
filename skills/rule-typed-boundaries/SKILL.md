---
name: rule-typed-boundaries
description: Parse external data into a typed model at the boundary and pass the model inside; no loose map or any past that line. A genuine open map is a map of string to string, not a model. A seam between components is an interface so the caller depends on the shape, not the implementation. From pstack's type-system-discipline and boundary-discipline, and dependency inversion.
disable-model-invocation: true
user-invocable: false
---

# Typed boundaries

## When

Data enters from outside: an HTTP body, a file, a config, a model's reply, an MCP result, a subprocess line. You are writing a signature and reach for a loose map or an escape hatch as a parameter or return (`dict`, `Any`, `object` in Python; `Record<string, any>`, `any`, `unknown` in TypeScript). Two components meet and one would import the other's concrete class.

## Rule

At the boundary, parse into a typed model (in Python a Pydantic model or a frozen dataclass; in TypeScript a type parsed from a schema) and fail closed on what does not fit: raise, do not guess. Past the boundary, pass the model; a loose map or an `any` inside is a boundary that was skipped. Name the data shape before writing the function that uses it. Where two components meet, the caller depends on an interface naming the methods it needs (a `Protocol` in Python, an `interface` in TypeScript), and the concrete class satisfies it structurally; that is the seam a test doubles and a second implementation plugs into.

A tuple of unnamed fields in a signature (`tuple[str, str]`, `list[tuple[str, int]]`) is a loose map too: the reader learns which field is which from a docstring or an unpacking. Name it as a model with named fields.

The exception, stated so it stays narrow: a genuinely open key-value map with no known keys (HTTP headers, environment variables, a JSON Schema object being printed) is correctly a map of string to string (or to a JSON value), not a model with no fields.

Instead of the tempting thing: do not thread a `dict` through three functions "because it is just JSON". The third function is where the KeyError lands.

## The test

For every loose map and escape hatch in a signature: which boundary did this come through, and why was it not parsed there?
