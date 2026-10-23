# Place by kind

A new module goes where the project keeps its kind. One older file of the same kind elsewhere is an outlier, not a precedent. From a correction, 2026-09-24, when model tools placed beside an outlier were moved in with the other tools.

## When

Creating a module, a package or a test file. Deciding where a new piece lives when the nearest similar file sits somewhere unusual. It does not apply to moving existing code for its own sake. That is a refactor with its own reason.

## Rule

Put new code where the project keeps things of its kind. That place is the layout in its rules file, the path a plan names, or the folder where most of its siblings live. Tools go with tools, services with services, a test beside the tests for that folder. Name it per **rule-name-for-the-reader**. One older file of the same kind somewhere else is an outlier, not a precedent. Leaving a path a plan names is a decision to raise before building, not one to take and report.

Instead of the tempting thing, do not put it beside the one similar file you happened to read first.

## The test

Cover the file name and point at its folder. Would someone who knows the layout look for it there? If they would look where its siblings live, it goes there.
