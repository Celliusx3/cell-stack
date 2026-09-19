---
name: rule-split-on-the-seam
description: One file, one responsibility. When a file nears the project's line cap, split it where the imports already divide; never raise the cap or exempt a file. The number lives in the project's CLAUDE.md. From the file-length rule projects state and the single-responsibility rule.
disable-model-invocation: true
---

# Split on the seam

## When

A file is within about forty lines of the project's cap (the number is in the project's `CLAUDE.md`; if there is none, three hundred). A module answers two different questions: it holds the data shapes and also decides what to do with them; it parses and also renders; it is a client and also a server. A new function does not fit the file's docstring.

## Rule

One file has one responsibility, stated in its first line. When it grows past that, split it where the imports already divide: the half that imports only the modelling library and nothing from the package is the data; the half that imports the data and a client is the decision. Name the new file for what it does, not for "utils" or "helpers". Never raise the cap, never add an exemption; the first exemption is the last time the rule meant anything.

Instead of the tempting thing: do not compress the file to fit (shorter names, dropped comments, merged functions). That buys a few lines and costs the reader.

## The test

Can you write the file's one-line purpose without an "and"? If not, the "and" is the seam.

## Example

A `ledger.py` whose first line is "Read a CSV ledger and answer questions about its rows" has an "and" in it. The seam is the import line: `load` needs `pathlib` and the row model; `total`, `by_month` and `largest` need only the rows. Split into `ledger/rows.py` (the model and `load`) and `ledger/questions.py` (the three questions), each with a first line that has no "and", each far from the cap.
