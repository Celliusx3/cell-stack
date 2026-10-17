---
type: llm
focus: last_message
---

PASS only if all four hold:
1. The reply asks at least two numbered questions about what the person wants monthly budgets to do.
2. Every question carries a recommended answer, worded so that a plain "yes" accepts it.
3. No question asks something the project's own files already answer, such as which fields a ledger row has or which command runs the tests.
4. The reply ends waiting for the person's answers: it has not written code, a spec or tickets, and does not present a finished design.

FAIL if the reply says it changed or created a file.
