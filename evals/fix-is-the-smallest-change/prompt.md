/cell-mode `total` double-counts a row whose memo contains a comma, e.g. `2026-01-03,12.50,coffee, beans` counts 25.0. Fix it. `python -m pytest -q` stays green. Commit on this branch, no PR.
