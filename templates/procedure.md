---
name: NAME
description: One line. The phrasings that should trigger it, and what it produces.
disable-model-invocation: true
---

# NAME

One sentence on what this procedure produces and for whom.

## Steps

1. First step. Name the evidence it produces.
2. Second step.
3. Present the result to the user.

## Subagents

If a step says "spawn", the prompt lives in `references/<role>-prompt.md` and is passed verbatim. Name the `subagent_type` (`Explore` for read-only, `general-purpose` when it writes) and whether `model` is set.

## Reply

What the reply must contain, in order.
