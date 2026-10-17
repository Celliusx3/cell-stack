# No name switch

Code that serves every member of a kind never branches on one member's name; the difference moves onto the member, or the shared code stays generic. The open/closed principle. From a correction on 2026-10-11, when two chat channels each grew a branch on one tool's name to pick a line of text, and the person called it not SOLID.

## When

Shared code (a channel, a dispatcher, a renderer, a router, a registry) gains a branch for one caller: a comparison against one name, a case for one kind, a lookup of one string. It does not apply inside the member itself, or to a table that lists every member the same way.

## Rule

Shared code knows no member by name. When one member needs something different there, either make the shared behaviour right for every member, or move the difference onto the member: a field on its declaration, or its entry in the map it registers in. Prefer the first; it deletes code.

Instead of the tempting thing: do not add the branch because it is one line. The next member copies it, and every shared file ends up listing the members.

## The test

Add a new member in your head. If any shared file needs a line for it, that file knows too much.
