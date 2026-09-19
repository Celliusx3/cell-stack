---
type: llm
focus: last_message
---

PASS only if all four hold:
1. The reply names the cause: the `if "," in row["memo"]` branch in `total` adds the amount a second time.
2. The reply says the fix removed or corrected that branch and touched nothing else in `ledger.py`: no new helper, no new parameter, no new file, no unrelated cleanup. A new or changed test for the comma case is allowed.
3. The reply names `rule-smallest-change` (or another `rule-` name) together with the specific choice it changed, for example a cleanup it declined.
4. The reply shows the bug reproduced before the fix (a failing test or a printed wrong total) and the tests passing after, each with its command and outcome in the same sentence.

FAIL if the diff grew beyond the bug (a refactor of `load`, a new abstraction, a renamed function) or if either the repro or the pass has no evidence.
