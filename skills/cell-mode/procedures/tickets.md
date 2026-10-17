# Tickets

Split a spec into tickets that Build takes one at a time, in order. The Feature playbook runs it after the spec, and so does the Refactor playbook for a refactor of more than about five files; it ends at the person's approval. Shaped after mattpocock's to-tickets skill.

## Steps

1. Cut the spec into vertical slices. Each ticket goes through every layer it needs (the stored data, the logic, what the person sees, its test) and leaves something a person can try; a ticket is never one layer on its own. Ticket 01 is the thinnest path from what the person does to what they see. A ticket is about five files or fewer, so one subagent can build it. For a refactor, a ticket is one piece of the end state instead, which leaves the tests green when it is done; its Checks are the tests that guard that piece's promises.
2. When the code needs reshaping before a ticket is easy, the reshaping is its own ticket ahead of it, with no change in behaviour. A change across many files is two tickets: add the new beside the old, then move the callers and delete the old.
3. Give each ticket its blockers: the tickets that must be done before it starts. Number the tickets in that order, blockers first.
4. Write one file per ticket beside the spec, `tickets/<NN>-<slug>.md`, numbered from 01, never one combined file. Each has:
   - **Status.** `open`. Build sets it to `done` in the ticket's commit.
   - **What to build.** The slice in two to four lines, naming the files and the data shape it touches.
   - **Checks.** The end-to-end check it must pass: what is run, and what comes out. Build writes this check first and watches it fail; a refactor ticket's check passes before and after.
   - **Blocked by.** The ticket numbers, or `none`.
5. Show the person the ticket list, one line each (number, what a person can try after it, blocked by), and every spec Decisions line marked "to decide at approval". This is the stop before Build, Feature's stop 2. Change the split until they approve; their approval also covers the commit Build makes for each ticket. When the person said not to ask, skip the stop and say so.

## Subagents

None.

## Reply

The ticket list, one line each, the decisions left open, and the request to approve.
