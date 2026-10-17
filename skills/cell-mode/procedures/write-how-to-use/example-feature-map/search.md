# Search notes

Search finds notes by title or body, opens a match in the editor, and tells a person the difference between no matches and search being unavailable.

## Sub-features

- `search-open` opens search from each browser entry point.
- `search-match` returns title and body matches without changing any note.
- `search-open-result` opens a result in the editor.
- `search-empty` shows an empty state for a query with no matches.
- `search-clear` removes the query and brings back recent notes.
- `search-cli` returns the same matches from the terminal.

## How to get to it (user POV)

- Choose the `Search` button in the toolbar.
- Press `/` while focus is outside an editable field.
- Run `notes search <query>` in a terminal.

## Using it with control-notes

Preconditions:

- Notes is healthy at `http://127.0.0.1:4173` and `control-notes doctor` agrees.
- The seed holds `Quarterly plan` with body text `Draft budget`.

- **Toolbar entry.** Run `control-notes browser click --role button --name "Search"`. A dialog named `Search notes` appears with focus in its searchbox.
- **Keyboard entry.** Close the dialog, then run `control-notes browser press --key "/"`. The same dialog appears and no slash is typed into the page.
- **Title match.** Run `control-notes browser fill --role searchbox --name "Search notes" --value "quarterly"`. The `Search results` list holds `Quarterly plan` and not `Grocery list`.
- **Body match.** Fill `budget` the same way. `Quarterly plan` stays, with a body excerpt.
- **Open result.** Run `control-notes browser click --role link --name "Quarterly plan"`. The dialog closes and the editor heading reads `Quarterly plan`.
- **Empty state.** Reopen search and fill `volcano`. A status named `No matching notes` appears.
- **Clear.** Run `control-notes browser click --role button --name "Clear search"`. The searchbox is empty and `Recent notes` is back.
- **CLI match.** Run `control-notes cli -- notes search "quarterly" --format json`. Exit code `0`, one object whose title is `Quarterly plan`.
- **CLI miss.** Run `control-notes cli -- notes search "volcano" --format json`. Exit code `0`, stdout `[]`.
- **Proof.** Run `control-notes browser snapshot --aria --path artifacts/search/results.aria.txt` and `control-notes browser screenshot --path artifacts/search/results.png`. Both show Notes, the query and `Quarterly plan`.

## Gotchas

- `/` inside the editor or the searchbox types a slash instead of opening search.
- Results arrive after a short debounce; wait for the list or the empty status, not a fixed sleep.
- Archived notes are left out unless `Include archived` is on.
- The CLI prints for people by default; use `--format json` for stable checks.
- Opening a result changes the page; reopen search before proving another query.
