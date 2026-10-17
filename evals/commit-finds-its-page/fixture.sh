#!/usr/bin/env bash
# The shared ledger project, then two uncommitted stories: the total fix with its test, and a README.
set -euo pipefail
bash "$(cd "$(dirname "$0")/.." && pwd)/fixture.sh"
git config user.name fixture
git config user.email fixture@example.com
python3 - <<'PY'
from pathlib import Path
p = Path("ledger.py")
p.write_text(p.read_text().replace('        if "," in row["memo"]:\n            result += row["amount"]\n', ""))
PY
cat >> test_ledger.py <<'PY'


def test_total_counts_a_memo_with_a_comma_once(tmp_path: Path) -> None:
    p = tmp_path / "l.csv"
    p.write_text("2026-03-01,5.00,tea, milk\n")
    assert total(load(p)) == 5.0
PY
cat > README.md <<'MD'
# ledgerkit

Prints a CSV ledger's total, each month's total and its largest row: `python cli.py ledger.csv`.
MD
