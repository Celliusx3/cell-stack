# Strip comments

Remove the comments a file does not need, and fix the code that needed them. The reader is whoever reads the file next. Ported from pstack's strip-comments skill and its Comment Sicko reviewer.

## Steps

1. Spawn one `Agent` with `subagent_type: "general-purpose"`. It reads every file in full and edits nothing. Evidence: its report, a list of deletions and `MUST KILL` flags with one line each.
   1. Pass it the prompt in `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/strip-comments/reviewer-prompt.md` verbatim.
   2. After the prompt, give the scope as file paths or a diff command.
   3. The scope is the caller's files or diff. Otherwise, it is the working tree's diff against the base branch (default `main`), uncommitted changes included.
   4. After the scope, paste the project's own comment and docstring rules word for word, with their file.
   5. Do not restate the reviewer's rules.
   6. Do not set `model`.
2. Inspect the report against the code.
   1. Reject any finding that edits application code, escapes the scope, or deletes one of the five exceptions.
   2. Reject a deletion that breaks a project rule pasted in the brief.
   3. Also reject a finding that misstates a `MUST KILL` reason, or treats intentional code as guilty.
   4. A comment the reviewer kept survives only with proof that it is about something we cannot change.
   5. On a thin `IMPORTANT` or `do not remove`, read the symbol and its callers yourself.
   6. An ambiguous kill stands. An ambiguous keep is deleted.
   7. If the report is unusable, rerun once with the failure named.
   8. If the second report is bad too, report it open. The procedure fails.
3. Delete the accepted comments.
   1. Fix the trivial `MUST KILL`s directly:
      - remove a dead path
      - drop a parameter
      - use the real API
      - rename the symbol, so the prose is unnecessary
4. For a `MUST KILL` that needs a new shape, sketch it in the reply in three lines.
   1. Stop there.
   2. Implement only the smallest root-cause fix inside the scope.
   3. Never add a symptom guard.
   4. Report root causes outside the scope as open.
5. Offer to encode a constraint comment about something we can change.
   1. A constraint comment is `do not remove`, `do not change wording`, or `talk to X before changing`.
   2. Offer the cheapest type, test, or lint inside the scope that encodes it.
   3. When a playbook runs this procedure, keep the comment. List the offer in the reply, and go on.
   4. When the person asked for this procedure, wait for them to accept.
   5. If they accept, encode it. Then delete the comment.
   6. If they decline, delete the comment. Report the constraint open.
6. Run the project's tests for the touched files.
   1. Paste the command and its outcome.

## Reply

Under twenty lines:

- The deletion count.
- The comments restored, with the exception each one met.
- The reruns.
- The `MUST KILL` flags fixed, sketched, or open, one line each.
- The encodings offered, and whether each was accepted.
- The test command and its outcome.
