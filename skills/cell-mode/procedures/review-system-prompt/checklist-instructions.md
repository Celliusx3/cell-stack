# Prompt checklist: instructions

How the prompt tells the model what to do. From Anthropic's prompt-engineering docs, the overview and the best-practices page for the current models. Last checked against those pages on 2026-11-13.

## Contents

1. Intent and context
2. Style for current models
3. Conflicts, gaps and dead text
4. Structure and format
5. Examples

## 1. Intent and context

- The prompt says what the model is for, who it talks to, and what a good result looks like.
- A role line such as "You are a support agent for X" helps only when the real context follows it.
- A rule comes with its reason. "Never use ellipses" works worse than "A speech engine reads your replies, and it cannot say ellipses."
- Test it like this. Would a capable new colleague with no background do the right thing from this prompt alone? Anything they would ask about is a gap.

## 2. Style for current models

Current Claude models follow instructions literally and closely. That changes what a good prompt looks like.

- **Ask for the behaviour you want.** The model does what you ask, not more. To get more, say so: "Make the edits, do not only suggest them."
- **Do not shout.** `CRITICAL`, `YOU MUST` and blocks in capitals were for older models. Current models apply them too widely. Tools get called when they should not, refusals widen, and one rule pushes out others. Keep strong words for one or two hard limits.
- **Say what to do.** "Write in prose paragraphs" works better than "Do not use markdown". A list of bans with no target leaves the model guessing.
- **Match the prompt to the output.** A prompt full of headings and bullets invites them back.
- **Do not script the thinking.** "Think about X before you answer" usually beats a rigid list of steps. A real business process is the exception.
- **Remove old lines against laziness.** "Be thorough, check everything twice" now causes slow, long answers.
- **State the scope of action.** An agent needs to know whether to act or only to propose.
- **State length and tone** when they matter.

## 3. Conflicts, gaps and dead text

- No two instructions conflict. Check across joined pieces, tool descriptions and per-tenant text. When rules conflict, the model picks one at random. This is often the most important finding.
- The prompt says which rule wins where rules can meet. An example is "A format the user asks for wins over the defaults above."
- Edge cases have an answer: empty input, a request out of scope, a failed tool, a forbidden request. The answer says what to do, not only "don't".
- Dead text goes. That is rules the model keeps anyway, repeated rules, history, notes for engineers, and rules for removed features.
- Facts that change, such as dates, prices and model names, are filled in per request or marked for upkeep.

## 4. Structure and format

- Sections are clearly apart. Use XML tags such as `<instructions>` and `<user_data>`, or headings, the same way throughout. Tags are closed.
- Untrusted content is wrapped and labelled as data. That covers user documents, search results, tool output and user profiles. This is the main defence against prompt injection in the prompt itself.
- Long documents go near the top, and the question goes near the end. Each document has its own tag with its source and date.
- When a program reads the output, the format is exact: a JSON shape, tag names or a template.
- For strict machine output, the API's structured output or a tool call is better than prose.
- Do not depend on a prefilled assistant turn. Newer models do not all support it.

## 5. Examples

This section is about example replies in a prompt. A tool description takes no example calls, per **rule-name-tools-exactly**.

- Examples are in `<example>` tags and marked as examples.
- There are three to five, and they differ. With only one, its length, words and topic show up in every answer.
- Every example obeys the prompt's own rules. An example that breaks a rule teaches the example.
- Examples cover hard cases too: a refusal done well, an unclear request, an edge case.
