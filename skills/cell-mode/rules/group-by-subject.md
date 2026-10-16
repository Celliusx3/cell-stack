# Group by subject

Functions that share an argument stay functions in one module named for the subject. They become methods on a class only when the class holds state the caller should not manage or hides a decision behind one name. From pstack's minimize-reader-load; the user's 2026-09-19 preference for grouping into a class was revised the same day, after a one-field class bought nothing.

## When

Two or more functions take the same thing as their first argument (the same rows, the same events, the same config), or you are about to add one. You are tempted to make them a class because they belong together.

## Rule

Leave them as functions, together in one module named for the subject. Sharing an argument is not state and hides nothing; a class around it is one more layer between the question and the answer, and the module name already shows the subject. A class is earned only when it does one of two things:

1. It holds state the caller should not see or manage: an open connection, a cache, a cursor, an accumulator that changes.
2. It hides a decision behind one name: which implementation runs, in what order, with what defaults, so a test double or a second implementation can stand in.

Then name it subject plus role (`OrderRepository`, `MailSender`), make its fields exactly what it hides, and name its methods for what they return (**rule-name-what-it-returns**). Keep pure what was pure.

Instead of the tempting thing: do not wrap a frozen value in a one-field class so the module shows its subject. Do not create a class of static methods, or one with no fields.

## The test

Cover the class name. What does an instance know that the caller does not, or decide that the caller should not? If the answer is "nothing, it holds the argument", it is functions.
