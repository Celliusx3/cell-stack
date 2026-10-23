---
type: llm
focus: last_message
---

PASS only if all three hold:
1. No sentence in the reply has more than 25 words. A word in backticks or a number counts as one word.
2. No numbered step has a sentence of more than 20 words.
3. Each numbered step tells one thing that happens. It can add one sentence for the result of that thing.

FAIL if any sentence joins two sentences with a semicolon, or if the reply contains an em dash.
