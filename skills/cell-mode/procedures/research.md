# Research

Find how others have built the thing before designing it, for whoever has to choose a shape: one read-only researcher per source, and a short table with links that leaves two or three options with a pick. Deep by facet, not by length.

## Steps

1. Pin the question in one line: what is being built, and what it must fit (a protocol, a library, a shape already in this project). Then list its facets, three to five sub-questions a row can answer (where it is stored, what the model sees each request, how it writes, the bounds, what the person sees). The facets go into every researcher's prompt.
2. Spawn the researchers in one message, each `subagent_type: "Explore"`, each given `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research/researcher-prompt.md` verbatim followed by the question, its facets, and one source line:
   - `Source: this project.` Its docs and code, for an existing pattern, a teardown, or a decision already written down.
   - `Source: GitHub.` `gh search code` and `gh search repos` for implementations of the same thing.
   - `Source: library docs.` Context7 (`resolve-library-id`, then `query-docs`) for each library involved.
   - `Source: the web.` Exa or WebSearch, in the first pass whenever the question is which shape to build; it waits for a thin result only when the question is how a named library behaves. You decide, and the reply says so.
   Each returns at most four rows: source, what they do, link or path, one quoted line. A second pass is one spawn per source not yet used, when the person asks for more or the pick is still open.
3. Read what comes back yourself. Drop any row with no link or path. Keep the quote, not the researcher's paraphrase. Count the sources behind each claim: a claim one source makes is marked "one source" in the table; a shape three or more build is the strong signal. A facet every researcher reported empty is named in the reply as a gap, not dropped.
4. Write nothing to the project unless asked; the table goes in the reply.

## Reply

Under twenty lines, in this order:

1. The one-line answer to the question the person asked, in their words, including whether an automatic or off-the-shelf way exists and why it is or is not the pick.
2. One table, at most six rows across all sources: source, what they do, link or path. When the rows fall into more than one shape, group the table by shape, name each shape as the choice it is, in everyday words ("write each one by hand", "generate them from the API"), and name who uses each; a label that needs explaining is not a name. The options are then the shapes.
3. The two or three options this leaves, one line each, with the pick and why. The first option is always adopt: an existing server, library or product, and its row carries stars, license, last push, and what it phones home to, so "adopt" is a checked claim.
4. Which sources were not used and why, in one line.
