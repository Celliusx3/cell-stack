**Status.** done

**What to build.** `git mv` `procedures/drive.md` to `procedures/write-how-to-use.md` and `procedures/drive/` to `procedures/write-how-to-use/`, with `feature-map/` renamed `example-feature-map/`. The skill the page saves is `how-to-use-<app>`, not `drive-<app>`. Every other "drive" in the page, its example, `playbooks/build.md` and `playbooks/fix.md` becomes a plain word: use, try, using it with. Update the mode's list.

**Checks.** `make check` passes before and after. `git grep -n -i driv -- skills` finds nothing. Break: leave the old path in Fix; lint fails.

**Blocked by.** 02
