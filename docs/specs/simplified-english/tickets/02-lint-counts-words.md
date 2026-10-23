**Status.** done

**What to build.** In `scripts/lint.sh`, run `scripts/long-sentences.py` on a list of rewritten pages. The list starts with `references/plan-file.md`. Replace the line caps with word caps:

- 950 words and 5 to 15 numbered steps for a playbook
- 2,700 words for `SKILL.md`
- 1,100 words for each other page under `skills/`

Add `scripts/same-meaning.py`, which compares a page with its copy at a base commit. Update the cap rows in `docs/adding-a-skill.md`.

**Checks.** Add a 30-word sentence to `references/plan-file.md`. `make lint` fails and names the file and the line. Remove the sentence, and `make lint` passes. `python3 scripts/same-meaning.py 2409dbd skills/cell-mode/references/plan-file.md` reports no loss.

**Blocked by.** 01
