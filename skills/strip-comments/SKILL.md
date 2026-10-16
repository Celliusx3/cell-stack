---
name: strip-comments
description: Strip comments before review. Spawn a read-only comment reviewer on the diff or the named files, delete what it finds, restructure what it marks MUST KILL, and offer an encoding for any comment that claims a constraint. Use for /strip-comments, "too many comments", "clean up the comments".
disable-model-invocation: true
user-invocable: false
---

# Strip comments

Removes the comments a file does not need and fixes the code that needed them, for whoever reads the file next. Ported from pstack's `/strip-comments` and its Comment Sicko reviewer; where pstack calls skills cellstack does not have, the step says what to do instead.

## Scope

The caller's files or diff. Otherwise the working tree's diff against the base branch, default `main`, including uncommitted changes.

## Steps

1. Spawn one `Agent` with `subagent_type: "Explore"` and the prompt in `references/reviewer-prompt.md` passed verbatim, followed by the scope (file paths, or the diff command). Do not restate its rules and do not set `model`. Evidence: its report, a list of deletions and `MUST KILL` flags with one line each.
2. Inspect the report against the code. Reject any finding that edits application code, escapes the scope, deletes one of the five exceptions, misstates a `MUST KILL` reason, or treats intentional code as guilty. A comment the reviewer kept survives only with proof it is about something we cannot change. Where pstack would run `/how` or `/why` on a thin `IMPORTANT` or `do not remove`, read the symbol and its callers yourself. An ambiguous kill stands; an ambiguous keep is deleted. Rerun once with the failure named if the report is unusable; a second bad report is reported open and the procedure fails.
3. Delete the accepted comments. Fix the trivial `MUST KILL`s directly: remove a dead path, drop a parameter, use the real API, rename the symbol so the prose is unnecessary.
4. For a `MUST KILL` that needs a new shape, sketch it in the reply in three lines and stop there; implement only the smallest root-cause fix inside the scope. Never add a symptom guard. Out-of-scope root causes are reported open.
5. A constraint comment (`do not remove`, `do not change wording`, `talk to X before changing`) about something we can change gets an offer: the cheapest in-scope type, test, or lint that encodes it. Wait for the person to accept. Accepted: encode, then delete the comment. Declined: delete the comment and report the constraint open.
6. Run the project's tests for the touched files and paste the command and its outcome.

## Subagents

The reviewer is `Explore`, which cannot write; its prompt lives in `references/reviewer-prompt.md`. No `model` is set.

## Reply

Deletion count. Comments restored, with the exception each one met. Reruns. `MUST KILL` flags fixed, sketched, or open, one line each. Encodings offered and whether each was accepted. The test command and its outcome. Under twenty lines.
