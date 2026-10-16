---
name: commit
description: Commit the working tree as one commit per story, each proven to pass on its own, in the repo's own message style. Use for /commit, "let's commit this", "commit this", or when a playbook's commit step is reached and the person asked for commits.
disable-model-invocation: true
user-invocable: false
---

# Commit

Turns a working tree that holds several stories into one commit per story, for a person who reads history one commit at a time. Each commit is proven to pass on its own. Nothing is pushed.

## Steps

1. Read what is there: `git status --short`, `git diff HEAD --stat`, and `git log -5` for the message style. Name anything untracked that was there before this work and is not yours; it stays out. Evidence: the changed paths, and what stays out.
2. Group the paths into stories, in this order: each fix, each feature, then a test or doc that spans them. A story is what one subject line can say. Evidence: a table of story to paths, with any path that two stories share marked.
3. Clear the staging area with `git reset`. The files on disk do not change; say that the person's staged selection is gone.
4. For each story, in order, stage its paths with `git add`. For a path two stories share, stage the in-between version: write the file as it should read after this story to a scratch path, then run `git update-index --cacheinfo 100644,$(git hash-object -w <scratch path>),<path>`. Evidence: `git diff --cached --stat` per story.
5. Write the message to a scratch file and commit with `git commit -F <file>`, alone in its command. The subject is `<type>: <what changes, in plain words>`, in the repo's own voice. The body says why first, then what, then the choice made. No attribution lines.
6. Prove each commit on its own: `git worktree add --detach <scratch>/<sha> <sha>`, run the project's test command inside it, and note the pass count. A commit that fails means the split was wrong: `git reset --mixed <base>` and redo from step 3; the files on disk never change. Evidence: one line per commit, the short hash and its pass count.
7. Remove the worktrees with `git worktree remove --force <path>`, then `git worktree prune`. Confirm `git diff HEAD` is empty and the untracked list is what step 1 left out.

## Subagents

None. Every step runs in the main conversation, since the split is a judgment about the person's own changes.

## Reply

The commits as a table, short hash and subject, oldest first. The pass count at each commit, and any failure that was there before this work. What stayed out, and that the staged selection was reset. Nothing pushed.
