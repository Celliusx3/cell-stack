---
name: typescript
description: How the rules are spelled in TypeScript. Applied to any .ts or .tsx file; read after the rule it spells.
disable-model-invocation: true
---

# TypeScript

Read the rule first; this is only how it is written here. One row per rule in the mode's index.

| Rule | In TypeScript |
|---|---|
| **rule-smallest-change** | No optional prop or parameter for a caller that does not exist, no `...rest` passed through "for later", no `try/catch` around a call that cannot throw. A new module needs an importer outside tests. |
| **rule-no-pass-through** | `const f = (x) => g(x)` is deleted; so is a re-export barrel nobody imports and a hook that only returns another hook's value. A wrapper survives only when it converts, defaults, checks, or translates an error. |
| **rule-split-on-the-seam** | The seam is the import block. A module that imports only the schema library (`zod`) and nothing from its own package is the data; a module that imports the data and `fetch`, a client, or React is the decision. Split at that line; name the new module for what it does, never `utils.ts` or `helpers.ts`. |
| **rule-typed-boundaries** | A typed model is a `z.object(...)` schema with `type X = z.infer<typeof X>`. Parse with `X.parse(raw)` at the boundary and let it throw: that is failing closed. Inside, no `any`, no `Record<string, any>`, no `as` cast, no tuple of unnamed fields (`[string, string]`) where an object with named fields would do; `unknown` only as the type of data not yet parsed. An interface is an `interface` or `type` the caller owns. A sum type is a discriminated union on a `kind` literal, with `const _exhaustive: never = x` in the default arm. A genuinely open map is `Record<string, string>`. |
| **rule-group-by-subject** | The functions stay exported functions in one module named for the subject. A class that is earned has `private readonly` fields for what it hides and is named subject plus role (`OrderRepository`, `MailSender`); methods are verb phrases. A closure factory returning an object of methods over the same hidden state is the same shape and is fine in a codebase that avoids `class`. No one-field wrapper around a value the caller already holds, no class of static methods. |

Also here: `unknown` over `any` for external data; `satisfies` over `as`; pass an object, not positional arguments, when a call has more than two; no `console.log` in shipped code.

Examples: `references/patterns.md`.
