---
type: llm
focus: last_message
---

PASS only if all seven hold:
1. The reply names the class a row is now parsed into inside `load` (a Pydantic model or a frozen dataclass), and says `currency` is a field on it with the USD default.
2. The reply says the functions after `load` receive that class, not `dict[str, Any]`, or names the one place a dict remains and why it is a genuinely open map.
3. The reply names `rule-typed-boundaries` (or another `rule-` name) together with the specific choice it changed.
4. Every claim that the tests pass carries the command and its outcome in the same sentence.
5. Before any implementation detail, the reply says what changes for the person running `cli.py`.
6. The reply contains a research table with at least one row that has a link or a path, and names the design pick with at least one alternative.
7. The reply shows the new test failing before the implementation and passing after, and the `cli.py` output with the currency column.

FAIL if `currency` was added as one more dict key with no model, if there is no research table, if the lead wrote the code itself with no subagent, or if a test claim has no evidence.
