---
type: llm
focus: last_message
---

PASS only if all five hold:
1. The reply has two labelled parts, Problem and then Explanation, as headings or bold lead words. An opening line or two saying what is being explained is allowed, and so are up to two short notes after the steps: a defect found nearby, or something that could not be run or checked. There is no analogy, no list of the thing's parts, no gotcha, caveats or things-to-know section, no summary, and no closing question to the reader.
2. The Problem part is two or three sentences saying what a person would have to do by hand, or would get wrong, without `by_month`.
3. The Explanation part is three to six short numbered steps that follow one example with specific dates and amounts through to what comes out: each month with its total. The totals are correct for the rows the example gives.
4. The opening line or the first numbered step says in plain words what `by_month` does.
5. No numbered step is about the explainer itself: what it read, which example it chose, or what it checked.

FAIL if the reply has more than fifteen non-blank lines, contains a code block, cites a file with a line number, or says it changed a file.
