---
type: llm
focus: last_message
---

PASS only if all four hold:
1. The verdict says the skill is ready, or ready after small changes.
2. The reply reports no High-severity finding.
3. The reply lists five findings or fewer.
4. No finding claims a problem the files contradict, such as a missing "when to use" clause, a missing file or nested references.

FAIL if any of these is missing.
