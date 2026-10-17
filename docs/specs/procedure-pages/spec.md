# Procedure pages that are found by name and say each thing once

## Problem

When you say "commit this", nothing in the mode points at the commit page, so Claude commits its own way. Playbooks send Claude to commands that do not exist, so it has to guess which page they mean. Each procedure page still carries what it had as a separate skill: a second opening, trigger words, a section that repeats the mode, and notes about pstack. One name, drive, reads as "drive the app now" when the page writes a skill for using the app.

## What changes for you

1. You type "commit this".
2. The mode lists every procedure beside its rules: when it applies, and where its page is. Claude opens the commit page.
3. A playbook step names the page it means by its path. No page names a command that does not exist.
4. The page opens with one line on what it makes, then its steps, then its reply.
5. When a fix has to be shown in the real app, Claude follows the repo's how-to-use skill, or writes one first with the page that used to be called drive.

What each procedure does stays the same.

## Decisions

- The mode lists every procedure, as it already lists every rule and playbook, and lint checks the list both ways, as it does for rules.
- A procedure is named by its full path, the form Feature already uses for grill, spec and tickets, so lint's path check covers it.
- Only drive is renamed: the page becomes write-how-to-use and the skill it saves becomes how-to-use-yourapp. The person picked the name.
- A page does not say which playbook runs it or at which step; the mode's list says when.
- Where a page came from stays in a few words; notes about pstack's other skills go.

## Out of scope

- Changing what any procedure does.
- The reviewer and researcher prompts.
- Renaming the drive skills already saved in other repos; each is its own change there.

## How we will know it works

- make check passes after every change, as it does today (lint clean, manifest valid).
- A new test case: on the sample ledger project with an uncommitted change, "commit this" opens the commit page.
- The strip-comments, feature-grills-first and feature-parses-at-the-boundary cases still pass.
- Removing a procedure from the mode's list makes lint fail, and so does a playbook naming a command that does not exist.
