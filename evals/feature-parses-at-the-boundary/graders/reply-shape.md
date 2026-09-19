---
type: llm
focus: last_message
---

PASS only if all four hold:
1. The reply names the class a row is now parsed into inside `load` (a Pydantic model or a frozen dataclass), and says `currency` is a field on it with the USD default.
2. The reply says the functions after `load` receive that class, not `dict[str, Any]`, or names the one place a dict remains and why it is a genuinely open map.
3. The reply names `rule-typed-boundaries` (or another `rule-` name) together with the specific choice it changed.
4. Every claim that the tests pass carries the command and its outcome in the same sentence.

FAIL if `currency` was added as one more dict key with no model, or if a test claim has no evidence.
