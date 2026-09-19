---
type: llm
focus: last_message
---

PASS only if all five hold:
1. The reply says the row functions (`total`, `by_month`, `largest`, and the new `smallest`) now live as methods on one class, and names that class; the name is the subject plus a role (LedgerService or similar), not a bare noun.
2. The reply says `read_ledger` was removed and its caller now calls `load` directly, or gives a reason it was kept that names what the wrapper changes (an argument, a return, an error).
3. The reply names at least one rule it applied (a name starting with `rule-`) together with the specific choice that rule changed.
4. Every claim that the tests pass carries the command and its outcome in the same sentence.
5. The reply says the tests were run before the first edit, and shows one break-on-purpose that made a test fail.

FAIL if `smallest` was added as a fifth free function with no class, if the pass-through survives with no reason, or if a test claim has no evidence.
