---
type: llm
focus: last_message
---

PASS only if all five hold:
1. The reply flags delete_workspace (or remove_member) as a destructive action with no confirmation rule, and gives text that requires confirmation.
2. The reply flags that the example uses headings, bullets and bold against the plain-prose rule.
3. The reply links the "Be extremely thorough. Check everything twice" block to the slow, rambling answers and says to remove or replace it.
4. The reply flags search_help and search_docs as overlapping with no rule for which to use.
5. The reply flags that nothing says what to do when the search finds nothing relevant.

FAIL if any of these is missing.
