#!/usr/bin/env bash
# The shared ledger, then a ledger.py rewritten with every kind of comment the
# reviewer must judge: banner, narration, a corpse, a false IMPORTANT, a noqa
# on a short line, and one genuine vendor-forced note that must survive.
set -euo pipefail
exec_root="$(cd "$(dirname "$0")/.." && pwd)"
bash "$exec_root/fixture.sh"
cat > ledger.py <<'PY'
"""Read a CSV ledger and answer questions about its rows."""

# ============================================================
# Ledger helpers
# ============================================================

import csv
from pathlib import Path
from typing import Any


def load(path: Path) -> list[dict[str, Any]]:
    # open the file and read the rows
    rows: list[dict[str, Any]] = []
    # csv needs newline="" on Windows or it doubles line endings, per the csv docs
    with path.open(newline="") as handle:
        for line in handle:
            # skip blank lines and headers
            if not line.strip() or line.startswith("#"):
                continue
            date, amount, memo = line.rstrip("\n").split(",", 2)
            rows.append({"date": date, "amount": float(amount), "memo": memo})
    return rows


def read_ledger(path: Path) -> list[dict[str, Any]]:
    return load(path)


# def old_total(rows):
#     return sum(r["amount"] for r in rows)


def total(rows: list[dict[str, Any]]) -> float:
    # IMPORTANT do not remove, crashes without it
    if rows is None:
        rows = []
    result = 0.0
    # loop over rows and add them up
    for row in rows:
        result += row["amount"]
        if "," in row["memo"]:
            result += row["amount"]
    return result


def by_month(rows: list[dict[str, Any]]) -> dict[str, float]:
    months: dict[str, float] = {}  # noqa: E501
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
git add -A && git -c user.name=fixture -c user.email=fixture@example.com commit -qm "comments"
