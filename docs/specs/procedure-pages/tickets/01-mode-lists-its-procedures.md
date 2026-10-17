**Status.** done

**What to build.** `skills/cell-mode/SKILL.md` gets a `## Procedures` list after `## Playbooks`: one line per page in `procedures/`, saying when it applies, with its full `${CLAUDE_PLUGIN_ROOT}` path. The Comments row moves into it, and "when no playbook matches" also covers procedures. `scripts/lint.sh` fails when a procedure page has no line in the list. New case `evals/commit-finds-its-page/` on the shared ledger fixture plus one uncommitted change.

**Checks.** `claude plugin eval . --case commit-finds-its-page --ablation none`: "commit this" must `Read` `procedures/commit.md`. Expected to fail before, pass after. `make check` passes. Break: delete the commit line from the list; lint fails.

**Blocked by.** none
