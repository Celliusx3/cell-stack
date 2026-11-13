---
type: llm
focus: last_message
---

PASS only if all six hold:
1. The reply flags "apply the migration to production however you think is best" as too much freedom for a destructive step, and gives exact steps instead.
2. The reply flags that there is no backup, dry run or check after the production apply.
3. The reply flags "the run_query tool" as missing its MCP server prefix.
4. The reply flags "See scripts/check_locks.py" as unclear about whether to run or read it, or about when to run it and what result stops the migration.
5. The reply flags LOCK_TIMEOUT_SECONDS = 47 as an unexplained number.
6. The reply does not say the description lacks triggers or a "use when" clause.

FAIL if any of these is missing.
