---
name: writing-changelogs
description: Writes a user-facing changelog entry or release notes from a range of git commits or merged pull requests. Use when the user asks for a changelog, release notes, "what changed since v2.3", a summary of a release for customers, or wants to update CHANGELOG.md, even if they only paste a list of commits. Not for writing commit messages or PR descriptions.
---

# Writing changelogs

Changelog readers are customers and support staff, not the engineers who wrote the code. They
want to know what they can now do, what behaves differently, and what they must change. Write
for them.

## 1. Collect the changes

- If the user gives a version range, run `git log --no-merges --pretty='%h %s' <from>..<to>` and,
  when the repo uses GitHub, `gh pr list --state merged --search "merged:>=<date>"` for PR titles
  and labels.
- If they paste commits, use those and don't fetch more.
- Read the PR description when a title is too terse to tell what changed for the user.

## 2. Sort and filter

Group entries under these headings, in this order, and omit empty groups:
**Breaking changes**, **New**, **Improved**, **Fixed**.

Leave out changes a user can't observe: refactors, test-only changes, CI, dependency bumps
without a user-visible effect. If you're unsure whether something is visible, keep it and mark it
with `(?)` so the user can decide.

## 3. Write each entry

One line per change, starting with what the user can now do or what is different, not with the
code that changed. Link the PR number at the end.

Example
Commit: `feat(export): stream CSV rows instead of buffering (#812)`
Entry: `- Large CSV exports now start downloading immediately instead of after the whole file is built. (#812)`

Every breaking change says what the user must do: "Rename `API_TOKEN` to `ACME_API_TOKEN` in
your environment before upgrading."

## 4. Hand it back

Show the entry in the chat. If the repo has a `CHANGELOG.md`, offer to insert it at the top in
the file's existing format (see `references/keep-a-changelog.md` for the common one), and only
write the file after the user agrees.
