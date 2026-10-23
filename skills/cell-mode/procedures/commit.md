# Commit

Turn a working tree that holds several stories into one commit per story. Each commit is proven to pass on its own and uses the repo's own message style. The reader is a person who reads history one commit at a time. Nothing is pushed.

## Steps

1. Read what is there. Evidence: the changed paths, the base, and what stays out.
   1. Run `git status --short`, `git diff HEAD --stat`, and `git log -5` for the message style.
   2. Note `git rev-parse HEAD` as the base.
   3. Name anything untracked that was there before this work and is not yours. It stays out.
2. Group the paths into stories. Evidence: a table of story to paths, with any path that two stories share marked.
   1. Put the stories in this order: each fix, each feature, then a test or doc that spans them.
   2. Make each story what one subject line can say.
3. Clear the staging area with `git reset`. The files on disk do not change.
   1. Tell the person that their staged selection is gone.
4. Stage each story's paths, in order. Evidence: `git diff --cached --stat` per story.
   1. For each story, stage its paths with `git add`.
   2. For a path two stories share, write the file as it should read after this story to a scratch path.
   3. Stage that in-between version with `git update-index --cacheinfo 100644,$(git hash-object -w <scratch path>),<path>`.
5. Commit each story.
   1. Write the subject as `<type>: <what changes, in plain words>`, in the repo's own voice.
   2. Write the body: why first, then what, then the choice made.
   3. Add no attribution lines.
   4. Write the message per the mode's Writing section, to a scratch file.
   5. Commit with `git commit -F <file>`, alone in its command.
6. Prove each commit on its own. Evidence: one line per commit, the short hash and its pass count.
   1. Run `git worktree add --detach <scratch>/<sha> <sha>`.
   2. Run the project's test command inside it.
   3. Note the pass count.
   4. If a commit fails, run `git reset --mixed <base>`. The split was wrong, and the files on disk never change.
   5. Redo from step 3.
7. Remove the worktrees.
   1. Run `git worktree remove --force <path>`.
   2. Run `git worktree prune`.
   3. Confirm that `git diff HEAD` is empty.
   4. Confirm that the untracked list is what step 1 left out.

## Reply

The commits as a table, short hash and subject, oldest first. The pass count at each commit, and any failure that was there before this work. What stayed out, and that the staged selection was reset. Nothing pushed.
