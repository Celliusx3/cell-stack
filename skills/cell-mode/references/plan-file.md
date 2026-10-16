# Plan mode

Claude's plan mode and cell mode stack; plan mode wins where they disagree. `/research` runs during planning; the plan carries one line per decision naming who else does it, and the full table goes in the reply, never the plan. In plan mode: match the playbook as usual, run its read-only steps now (reading, tests, naming the shape, the end state), and put the rest into the plan file. Each playbook that writes marks where plan mode stops. After approval, open the todo list and resume the playbook at the first step after that mark; do not redo the read-only steps. Investigate and Explain never write, so plan mode changes nothing for them.

The plan file is written for a person deciding yes or no. Keep it simple: under fifty lines, one idea per section, and a section that runs past ten lines is cut, not explained. Lead each section with one concrete example (what the person says, what they see, what happens) before any list or table; a plan the person cannot picture is not ready. In this order:

- **What it does.** One sentence a person who never saw the code would follow: what this changes, for whom, and what it leaves alone. Then one example of the difference. With the next section, this is plan mode's Context.
- **The problem.** What is hard to read or wrong today, one short paragraph, no rule recital.
- **The idea.** For a feature: one walkthrough, numbered, of a person using it ("You say X. A card appears with Y. You tap Z, and..."). For a refactor: the end state as a story in plain words, five to ten lines, one verb per line, indented like code: no file names, no signatures, no `yield`. The shape that landed:
  ```
  checkout(order):
      look at the order
      if it is already paid:     done
      if the cart is empty:      refuse, done
      write STARTED
      charge the card            (one call, returns PAID or FAILED)
      write the result
  ```
  One block per idea. A helper the story calls does not get a second block: it gets a sentence, or a short list where every line is "question: answer". Where the callers sit is one line each after the block, not inside it. Every line of the block is "do this" or "if this: then that"; a line with no verb is a table row that wandered in. When the plan changes something the person has already met, each item is a before and after: what happened (their words, or the command and its output) and what happens next time.
- **Decisions.** One line each: the choice, and who else does it the same way. No table of sources here; that is the reply's.
- **What changes.** For a feature: the files, one line each saying what the file gains, grouped by commit. Anything the change stores says where it is kept, in what form, and who can read it. For a refactor: a before / after table, one row per moved or deleted thing, then the callers one line each, then the files touched as a count. More than about five files: two pieces, shown separately.
- **What does not change.** The promises the code keeps, and the tests that guard them, as a table of promise to test name. Count the baseline run ("31 passed"). A promise with no test is named here as the first thing to write. For a feature this may be one line: the baseline count and the test files that must stay green.
- **Later.** Things this plan deliberately leaves out, one line each, saying why nothing here changes for them.
- **A question, if there is one.** A behaviour choice the reshape exposes, in three lines: the case as one example, what the source being copied does there, and the strict option named.
- **Order of work.** The playbook's remaining steps, numbered, one line each, with the break-on-purpose named per piece.
- **Verify.** The commands and what green looks like.

Cell mode's Reply rules apply to the plan file too: everyday words, no `file:line` outside the tables, no paragraph where a table row will do.
