# Research

Find how others have built the thing before designing it. The reader is whoever has to choose a shape. Use one read-only researcher per source, and a short table with links that leaves two or three options with a pick. Deep by facet, not by length.

## Steps

1. Pin the question in one line.
   1. Say what is being built.
   2. Say what it must fit: a protocol, a library, or a shape already in this project.
   3. List its facets: three to five sub-questions that a row can answer. Typical facets are:
      - where it is stored
      - what the model sees each request
      - how it writes
      - the bounds
      - what the person sees
   4. Put the facets into every researcher's prompt.
2. Spawn the researchers in one message.
   1. Give each one `subagent_type: "Explore"`.
   2. Give each one `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/research/researcher-prompt.md` verbatim, followed by the question, its facets, and one source line:
      - `Source: this project.` Its docs and code, for an existing pattern, a teardown, or a decision already written down.
      - `Source: GitHub.` `gh search code` and `gh search repos` for implementations of the same thing.
      - `Source: library docs.` Context7 (`resolve-library-id`, then `query-docs`) for each library involved.
      - `Source: the web.` Exa or WebSearch, in the first pass whenever the question is which shape to build. It waits for a thin result only when the question is how a named library behaves. You decide, and the reply says so.
   3. Expect each researcher to return at most four rows: source, what they do, link or path, one quoted line.
   4. When the person asks for more, or the pick is still open, make a second pass.
   5. In a second pass, spawn one researcher per source not yet used.
3. Read what comes back yourself.
   1. Drop any row with no link or path.
   2. Keep the quote, not the researcher's paraphrase.
   3. Count the sources behind each claim.
   4. Mark a claim that only one source makes as "one source" in the table. A shape that three or more build is the strong signal.
   5. In the reply, name a facet that every researcher reported empty as a gap. Do not drop it.
4. Write nothing to the project unless asked. The table goes in the reply.

## Reply

Under twenty lines, written per the mode's Writing section, in this order:

1. The one-line answer to the question the person asked, in their words. Say whether an automatic or off-the-shelf way exists, and why it is or is not the pick.
2. One table, at most six rows across all sources: source, what they do, link or path.
   1. When the rows fall into more than one shape, group the table by shape.
   2. Name each shape as a choice, in everyday words: "write each one by hand", "generate them from the API".
   3. Name who uses each shape. A label that needs explaining is not a name.
   4. The options are then the shapes.
3. The two or three options this leaves, one line each, with the pick and why.
   1. The first option is always adopt: an existing server, library or product.
   2. Its row carries stars, license, last push, and what it phones home to. So "adopt" is a checked claim.
4. Which sources were not used and why, in one line.
