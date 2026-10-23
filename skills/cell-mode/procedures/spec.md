# Spec

Write the agreed change down as one file. The person approves it, and Build checks the finished code against it. Shaped after mattpocock's to-spec skill.

## Steps

1. Pick the folder. Evidence: the path, and why it is there.
   1. Use the folder where the project already keeps specs or plans, from its `CLAUDE.md` or the folders it has.
   2. If the project has none, use `docs/specs/<feature>/`, named for the feature in two to four plain words.
2. Write `spec.md` in that folder from the grill's agreed answers and the research table.
   1. Write it per the mode's Writing section.
   2. Give it these sections, in this order:
      - **Problem.** What the person cannot do today, in their words, in two or three sentences.
      - **What changes for you.** A numbered walkthrough of a person using it, one action in each step: what they do, and what they see.
      - **Decisions.** One line each: the choice, and who else makes it the same way, from the research table. When a research pick differs from a grill answer, write both. Mark the line "to decide at approval".
      - **Assumptions.** The recommended answers taken without asking, when the person said not to ask. Leave the section out otherwise.
      - **Out of scope.** What this feature leaves out on purpose, one line each.
      - **How we will know it works.** The checks a person could run, each as what they do and what they should see.
3. For a refactor, write the spec from the Refactor playbook's promises, what the change makes better, and its end state.
   1. Write Problem as what is hard to read or change today.
   2. In What changes for you, say that nothing a person sees changes.
   3. Then say how the code reads after the change.
   4. Write How we will know it works as the tests that guard the promises, with today's count.
   5. Leave out Decisions when there are none.
4. Keep file paths, function names and code out of the spec. They go stale, and the tickets carry them. Evidence: the file and its line count.

## Reply

The spec's path, and every Decisions line marked "to decide at approval".
