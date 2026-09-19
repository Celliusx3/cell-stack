#!/usr/bin/env bash
# Seeds a small project into the current (empty) workspace. Shared by every case.
# It carries every smell the principles target, so one fixture serves all cases:
# three functions on one subject, rows as dict[str, Any], and a pass-through.
set -euo pipefail
git init -q -b main
cat > CLAUDE.md <<'MD'
# ledgerkit

Reads CSV ledgers and prints totals. `python cli.py ledger.csv`.

Rules: every file under 120 lines. `python -m pytest -q` must stay green.
MD
cat > ledger.py <<'PY'
"""Read a CSV ledger and answer questions about its rows."""

from pathlib import Path
from typing import Any


def load(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        date, amount, memo = line.split(",", 2)
        rows.append({"date": date, "amount": float(amount), "memo": memo})
    return rows


def read_ledger(path: Path) -> list[dict[str, Any]]:
    return load(path)


def total(rows: list[dict[str, Any]]) -> float:
    result = 0.0
    for row in rows:
        result += row["amount"]
        if "," in row["memo"]:
            result += row["amount"]
    return result


def by_month(rows: list[dict[str, Any]]) -> dict[str, float]:
    months: dict[str, float] = {}
    for row in rows:
        month = row["date"][:7]
        months[month] = months.get(month, 0.0) + row["amount"]
    return months


def largest(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    best = None
    for row in rows:
        if best is None or row["amount"] > best["amount"]:
            best = row
    return best
PY
cat > cli.py <<'PY'
import sys
from pathlib import Path

from ledger import by_month, largest, read_ledger, total

rows = read_ledger(Path(sys.argv[1]))
print("total", total(rows))
for month, amount in sorted(by_month(rows).items()):
    print(month, amount)
top = largest(rows)
if top is not None:
    print("largest", top["memo"], top["amount"])
PY
cat > test_ledger.py <<'PY'
from pathlib import Path

from ledger import by_month, largest, load, total

SAMPLE = "2026-01-03,12.50,coffee\n2026-01-09,40.00,books\n2026-02-01,8.00,bus\n"


def rows(tmp_path: Path):
    p = tmp_path / "l.csv"
    p.write_text(SAMPLE)
    return load(p)


def test_total(tmp_path: Path) -> None:
    assert total(rows(tmp_path)) == 60.5


def test_by_month(tmp_path: Path) -> None:
    assert by_month(rows(tmp_path)) == {"2026-01": 52.5, "2026-02": 8.0}


def test_largest(tmp_path: Path) -> None:
    top = largest(rows(tmp_path))
    assert top is not None and top["memo"] == "books"
PY
printf '2026-01-03,12.50,coffee\n2026-01-09,40.00,books\n' > ledger.csv
git add -A && git -c user.name=fixture -c user.email=fixture@example.com commit -qm "seed"
