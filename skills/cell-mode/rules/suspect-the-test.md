# Suspect the test

When passing a test needs a shape you would not otherwise choose, the test is the suspect, not the code. Check what the test actually exercises before widening anything to satisfy it. The user's decision, 2026-09-23.

## When

A test is red and the fix that would turn it green is one you would not write on its own: widening a route or a match pattern, loosening a type, adding a branch for a case the caller cannot reach, reconstructing an input the layer below already normalised. Also when a subagent reports that it could not satisfy the brief and worked around it, and the workaround is in the code rather than the test.

## Rule

Stop and ask what the test actually exercises. Run the thing it claims to test, on its own, and look at what reaches the code under test. A test that asserts on behaviour of the client, the framework, the transport or the standard library is testing someone else's code, and the shape it is forcing on yours is rent you are paying for nothing.

Fix the test. Then, if the real case still exists, write the test that reaches it.

Instead of the tempting thing: do not widen the production shape and move on because the suite is green. Green bought that way hides two failures at once, the one the test never covered and the one the widened shape now allows.

## The test

Write the line you are about to change and ask: would I write this if the test did not exist? If no, the test is the suspect.
