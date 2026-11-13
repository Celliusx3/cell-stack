# Prompt checklist: tools, grounding and cost

The second half of the prompt checklist. Use each section only when it applies.

## Contents

1. Tools and agents
2. Grounding and honesty
3. Cost and caching
4. `CLAUDE.md` and `AGENTS.md`

## 1. Tools and agents

Check this section only when the model has tools.

- Each tool description says what the tool does, when to use it, when not to use it, and what comes back.
- Each argument's rule sits on that argument. A tool description has no example calls, per **rule-name-tools-exactly**.
- Two tools that overlap have a rule that says which one to use.
- The prompt says when to call tools in parallel, and when to wait for one result before the next call.
- An action that cannot be undone needs the user's confirmation or a clear scope. That covers delete, send, pay and deploy.
- A rule in the prompt lowers the risk of a destructive action but cannot remove it. Say when the tool itself must check.
- A long task says how to track progress, what to do when context runs low, and when to stop and ask.
- The model checks its own work where it can, and does not claim a success it did not check.
- No instruction pushes the model to special-case tests or hard-code answers.

## 2. Grounding and honesty

- The model may say it does not know, or that the sources do not answer the question.
- An answer from documents comes from the given material, cites or quotes it, and says when it is missing.
- When a search finds nothing relevant, the prompt says what to do instead of guessing.
- An agent that reads code or data reads it before it makes a claim.
- A safety or policy rule names exactly what is out of bounds and what the safe reply is. A vague, broad ban makes the model refuse too often.

## 3. Cost and caching

- Prompt caching reuses the longest prefix that did not change.
- Fixed content goes first: instructions, tool definitions and examples.
- Content that changes per request goes after it: timestamps, the user's name, search results and request ids.
- A timestamp at the top breaks the cache on every request.
- The size fits the job. Flag a section that could load only when needed, such as a skill, a tool result or a search result.
- Text repeated across prompt variants can be one shared block.

## 4. `CLAUDE.md` and `AGENTS.md`

A coding agent loads these files at the start of every session, next to its own system prompt. They stack: the root file, every folder file on the path, and each `@` import.

- Each line prevents a mistake the agent would otherwise make: a rule, a command or a trap. Explanations, designs and history go in docs, with a link.
- The file is short, because it costs tokens on every task.
- Commands are exact and can be copied. The paths and scripts it names exist.
- The root file and folder files do not conflict. A folder file narrows the root file and does not repeat it.
- A mirror file, such as an `AGENTS.md` made from a `CLAUDE.md`, matches its source.
- The style rules in `checklist-instructions.md` apply here too.
- Caching and per-request content apply only in part. The agent harness owns caching.
