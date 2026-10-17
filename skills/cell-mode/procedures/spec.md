# Spec

Write the agreed change down as one file the person approves and Build checks the finished code against. Shaped after mattpocock's to-spec skill.

## Steps

1. Pick the folder: where the project already keeps specs or plans, from its `CLAUDE.md` or the folders it has; if it has none, `docs/specs/<feature>/`, named for the feature in two to four plain words. Evidence: the path, and why it is there.
2. Write `spec.md` in that folder from the grill's agreed answers and the research table, with these sections in order:
   - **Problem.** What the person cannot do today, in their words, in two or three sentences.
   - **What changes for you.** A numbered walkthrough of a person using it: what they do, and what they see.
   - **Decisions.** One line each: the choice, and who else makes it the same way, from the research table. When a research pick differs from a grill answer, write both and mark the line "to decide at approval".
   - **Assumptions.** The recommended answers taken without asking, when the person said not to ask. Leave the section out otherwise.
   - **Out of scope.** What this feature deliberately leaves out, one line each.
   - **How we will know it works.** The checks a person could run, each as what they do and what they should see.
3. For a refactor, write it from the Refactor playbook's promises, what the change makes better, and its end state. Problem is what is hard to read or change today. What changes for you says that nothing a person sees changes, then how the code reads after. How we will know it works is the tests that guard the promises, with today's count. Leave out Decisions when there are none.
4. Keep file paths, function names and code out of the spec; they go stale, and the tickets carry them. Evidence: the file and its line count.

## Reply

The spec's path, and every Decisions line marked "to decide at approval".
