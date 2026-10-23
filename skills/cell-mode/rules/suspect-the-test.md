# Suspect the test

When passing a test needs a shape you would not otherwise choose, the test is the suspect, not the code. Check what the test actually exercises before widening anything to satisfy it. The user's decision, 2026-09-23.

## When

A test is red, and the fix that would turn it green is one you would not write on its own:

- widening a route or a match pattern
- loosening a type
- adding a branch for a case the caller cannot reach
- reconstructing an input the layer below already normalised

It also applies when a subagent could not satisfy the brief and reports a workaround. That workaround is in the code, not the test.

## Rule

Stop, and ask what the test actually exercises. Run the thing it claims to test, on its own. Look at what reaches the code under test. A test that asserts on behaviour of the client, the framework, the transport or the standard library is testing someone else's code. The shape it forces on yours is rent you pay for nothing.

Fix the test. Then, if the real case still exists, write the test that reaches it.

Instead of the tempting thing, do not widen the production shape and move on because the suite is green. Green bought that way hides two failures at once. One is the failure the test never covered. The other is the failure the widened shape now allows.

## The test

Write the line you are about to change, and ask: would I write this if the test did not exist? If no, the test is the suspect.
