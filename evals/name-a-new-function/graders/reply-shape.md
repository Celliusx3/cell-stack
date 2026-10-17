---
type: llm
focus: last_message
---

PASS only if all three hold:
1. The reply names the function it added to ledger.py.
2. That name tells a reader what the caller gets back (for example the report's lines) or what it does with its object (for example printing the report), without opening the function.
3. The reply names `rule-name-for-the-reader` together with the naming choice it changed.

FAIL if the new function's name is a bare verb or a bare noun that fits anything (report, render, run, process, summary), or if the reply does not name the function.
