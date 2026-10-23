**Status.** done

**What to build.** Add a `## Writing` section to `skills/cell-mode/SKILL.md`, before `## Reply`, in ten lines or fewer. It names the texts it covers. Its rules are direct sentences, one action in each numbered step, one word for one thing, the word caps, everyday words, and no em dash. Move the two style bullets out of `## Reply`.

Rewrite `skills/cell-mode/references/plan-file.md` so that it points at the Writing section and follows it. Add `scripts/long-sentences.py`, which prints each sentence over the caps with its file and line. Add the grader `evals/explain-in-two-parts/graders/short-sentences.md`.

**Checks.** `python3 scripts/long-sentences.py skills/cell-mode/references/plan-file.md` exits 1 before the rewrite and 0 after it. The Writing section passes the same script. `make check` passes.

**Blocked by.** none
