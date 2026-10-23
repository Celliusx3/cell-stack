**Status.** done

**What to build.** Rewrite `docs/adding-a-skill.md` and `README.md` in the Writing style. Change `scripts/lint.sh` so that it checks every page under `skills/` and `templates/`, plus those two docs, and delete the list. The old specs in `docs/specs/` stay out. Delete `scripts/same-meaning.py`.

**Checks.** `make check` passes with no list in `scripts/lint.sh`. A 30-word sentence added to any rule page makes `make lint` fail.

**Blocked by.** 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11
