---
name: research
description: Find how others have built the thing before designing it. Spawns one read-only researcher per source (this project, GitHub, library docs, the web) and returns a table with links and two or three options with a pick. Deep by facet, not by length; all four sources when the shape is open. Use for /research, "how do others do this", "what does the library say", and as step 3 of the Feature playbook.
disable-model-invocation: true
---

# Research

Evidence before design, for whoever has to choose a shape: a short table of what exists, with links, and the options it leaves.

## Steps

1. Pin the question in one line: what is being built, and what it must fit (a protocol, a library, a shape already in this project). Then list its facets, three to five sub-questions a row can answer (where it is stored, what the model sees each request, how it writes, the bounds, what the person sees). The facets go into every researcher's prompt.
2. Spawn the researchers in one message, each `subagent_type: "Explore"`, each given `references/researcher-prompt.md` verbatim followed by the question, its facets, and one source line:
   - `Source: this project.` Its docs and code, for an existing pattern, a teardown, or a decision already written down.
   - `Source: GitHub.` `gh search code` and `gh search repos` for implementations of the same thing.
   - `Source: library docs.` Context7 (`resolve-library-id`, then `query-docs`) for each library involved.
   - `Source: the web.` Exa or WebSearch, in the first pass whenever the question is which shape to build; it waits for a thin result only when the question is how a named library behaves. You decide, and the reply says so.
   Each returns at most four rows: source, what they do, link or path, one quoted line. A second pass is one spawn per source not yet used, when the person asks for more or the pick is still open.
3. Read what comes back yourself. Drop any row with no link or path. Keep the quote, not the researcher's paraphrase. Count the sources behind each claim: a claim one source makes is marked "one source" in the table; a shape three or more build is the strong signal. A facet every researcher reported empty is named in the reply as a gap, not dropped.
4. Reply. In plan mode, the same table goes into the plan file under "What others do". No file is written to the project unless asked.

## Subagents

Every researcher is `Explore` (it cannot write); the prompt lives in `references/researcher-prompt.md`; no `model` is set. All are spawned in one message so they run together.

## Reply

Under twenty lines. One table, at most six rows across all sources: source, what they do, link or path. When the rows fall into more than one shape, group the table by shape and name who uses each; the options are then the shapes. Then the two or three options this leaves, one line each, with the pick and why. The first option is always adopt: an existing server, library or product, and its row carries stars, license, last push, and what it phones home to, so "adopt" is a checked claim. Then which sources were not used and why, in one line.
