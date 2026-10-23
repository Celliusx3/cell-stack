# Typed boundaries

Parse external data into a typed model at the boundary, and pass the model inside. No loose map or any goes past that line. A genuine open map is a map of string to string, not a model. Where two components meet, the caller depends on an interface, so it depends on the shape, not the implementation. From pstack's type-system-discipline and boundary-discipline, and dependency inversion.

## When

Data enters from outside: an HTTP body, a file, a config, a model's reply, an MCP result, a subprocess line. You are writing a signature, and you reach for a loose map or an escape hatch as a parameter or a return. In Python that is `dict`, `Any` or `object`. In TypeScript it is `Record<string, any>`, `any` or `unknown`. Two components meet, and one would import the other's concrete class.

## Rule

At the boundary, parse into a typed model, and fail closed on what does not fit. In Python, the model is a Pydantic model or a frozen dataclass. In TypeScript, it is a type parsed from a schema. To fail closed, raise an error. Do not guess.

Past the boundary, pass the model. A loose map or an `any` inside is a boundary that was skipped. Name the data shape before writing the function that uses it.

Where two components meet, the caller depends on an interface naming the methods it needs: a `Protocol` in Python, an `interface` in TypeScript. The concrete class satisfies it structurally. That is where a test double or a second implementation plugs in.

A tuple of unnamed fields in a signature (`tuple[str, str]`, `list[tuple[str, int]]`) is a loose map too. The reader learns which field is which from a docstring or an unpacking. Name it as a model with named fields.

One narrow exception exists. A genuinely open key-value map with no known keys is correctly a map of string to string. It can also map to a JSON value. It is not a model with no fields. Examples are HTTP headers, environment variables, and a JSON Schema object being printed.

Instead of the tempting thing, do not thread a `dict` through three functions "because it is just JSON". The third function is where the KeyError lands.

## The test

For every loose map and escape hatch in a signature, ask: which boundary did it come through, and why was it not parsed there?
