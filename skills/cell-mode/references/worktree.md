# Moving work between a worktree and the checkout

How longer work moves between its worktree and the person's own checkout. The mode sends you here when work changes place.

## Into the checkout

Work comes back to the checkout only when the person asks to see it. Then:

1. Stash it in the worktree with its untracked files.
2. Remove the worktree.
3. Switch the checkout to the task's branch.
4. Pop the stash there.

## Back to a worktree

The next task that is longer work moves it back before its first edit:

1. Stash it with its untracked files.
2. Return the checkout to the branch it was on.
3. Add the worktree on the task's branch.
4. Pop the stash there.

## Syncing a branch

Before you move a local branch to match its remote, check that every commit only the local branch has is already upstream. A squash merge gives it a new hash, so compare the files, not the hashes.
