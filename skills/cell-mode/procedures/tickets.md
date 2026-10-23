# Tickets

Split a spec into tickets that Build takes one at a time, in order. The procedure ends at the person's approval. Shaped after mattpocock's to-tickets skill.

## Steps

1. Cut the spec into tickets. Each ticket is a vertical slice.
   1. Take each ticket through every layer it needs: the stored data, the logic, what the person sees, and its test.
   2. Make each ticket leave something a person can try. A ticket is never one layer on its own.
   3. Make ticket 01 the thinnest path from what the person does to what they see.
   4. Keep a ticket to about five files or fewer, so one subagent can build it.
   5. For a refactor, make a ticket one part of the end state instead. It leaves the tests green when it is done.
   6. For a refactor ticket, write as its Checks the tests that guard the promises of that part.
2. Put a reshaping or a change across many files in tickets of its own.
   1. When the code needs reshaping before a ticket is easy, make the reshaping its own ticket ahead of it.
   2. Give that ticket no change in behaviour.
   3. Split a change across many files into two tickets.
   4. The first ticket adds the new beside the old.
   5. The second ticket moves the callers and deletes the old.
3. Order the tickets by their blockers.
   1. Give each ticket its blockers: the tickets that must be done before it starts.
   2. Number the tickets in that order, blockers first.
4. Write one file per ticket beside the spec, `tickets/<NN>-<slug>.md`, numbered from 01.
   1. Never write one combined file.
   2. Write each file per the mode's Writing section.
   3. Give each file these parts:
      - **Status.** `open`. Build sets it to `done` in the ticket's commit.
      - **What to build.** The ticket in two to four lines, naming the files and the data shape it touches.
      - **Checks.** The end-to-end check it must pass: what is run, and what comes out. Build writes this check first and watches it fail. A refactor ticket's check passes before and after.
      - **Blocked by.** The ticket numbers, or `none`.
5. Stop for the person's approval of the tickets.
   1. Show the person the ticket list, one line each: number, what a person can try after it, blocked by.
   2. Show every spec Decisions line marked "to decide at approval".
   3. Stop here. This is the stop before Build, Feature's stop 2.
   4. Change the split until the person approves. Their approval also covers the commit Build makes for each ticket.
   5. When the person said not to ask, skip the stop. Say that you skipped it.

## Reply

The ticket list, one line each, the decisions left open, and the request to approve.
