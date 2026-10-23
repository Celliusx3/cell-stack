**Status.** done

**What to build.** Add `hooks/sentence-nag.sh` beside `hooks/comment-nag.sh`. After an `Edit` or a `Write` to a `.md` file under a `plans` or a `specs` folder, it runs `scripts/long-sentences.py` on the file. When the script finds long sentences, the hook tells the model to split them. It never stops the write. Register it in `hooks/hooks.json`. Add it to the syntax check in `Makefile` and to the hook paragraph in `README.md`.

**Checks.** Feed the hook a plan file with a 30-word sentence. It prints a message that names the file and the count. Feed it a plan file with short sentences. It prints nothing. Feed it a `.py` file. It prints nothing. `make check` passes.

**Blocked by.** 01
