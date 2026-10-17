# One naming rule, and a cleanup of the rule pages

## Problem

The only naming rule covers functions, and its example for an action is one bare verb. So Claude writes names like apply, repair and drained, which only make sense after opening the function. Folders have no naming rule, classes have half a sentence, and two rules disagree on how to name a file. Two rule names are hard to read, two rules use "decision" for opposite halves of the same code, and the TypeScript page contradicts the parameter rule.

## What changes for you

1. You ask Claude to add a /stop command to a chat bot.
2. Claude reads one naming rule that covers folders, files, classes, functions and tests.
3. It names the function for what happens, run_command, not apply. A bare verb is only used when the thing it is called on already names the object.
4. The new file is named for its subject in its folder's words, never utils or helpers.
5. A new folder is named for the subject its files share. A new class is a plain noun, or the subject plus its job, never Manager or Helper.
6. When Claude cites a rule in a reply, the name reads in everyday words: one job per file, name tools exactly.

## Decisions

- One naming rule for every kind of name, with one line per kind. Swift's API guidelines, cfcosta/duskpi's code-naming skill and databasus's agent rules do the same.
- A function that returns something is named for the value; one that acts is named with a verb. Google's Go guide and Swift's guidelines.
- A bare verb is fine when the module already names the object. Google's Go guide.
- A past participle names a returned value only, never a function that acts. Swift's guidelines.
- No utils, helpers or common for files and folders. stablyai/orca's agent rules and Google's Go guide.
- No Manager, Helper or Processor for classes unless the project uses the word. gitbutler's agent rules.
- TypeScript follows the same four-parameter limit as Python.

## Out of scope

- Renaming the vague names in the project the examples came from.
- Splitting the type rule, which does three jobs but is not wrong.

## How we will know it works

- make check passes after every ticket, as it does today.
- A new test case where Claude adds a function to the sample ledger project passes: Claude opens the naming rule and picks a name that says what comes back.
- The existing refactor test case still passes.
- Removing the naming rule from the mode's index makes lint fail.
