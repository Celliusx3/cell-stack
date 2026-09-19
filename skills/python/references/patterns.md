# Python patterns

One before / after per rule.

## rule-typed-boundaries

Before:
```python
def load(path: Path) -> list[dict[str, Any]]:
    return [{"date": d, "amount": float(a), "memo": m} for d, a, m in _rows(path)]

def total(rows: list[dict[str, Any]]) -> float:
    return sum(r["amount"] for r in rows)
```

After:
```python
class Row(BaseModel):
    model_config = ConfigDict(frozen=True)
    date: str
    amount: float
    memo: str

def load(path: Path) -> list[Row]:
    return [Row.model_validate({"date": d, "amount": a, "memo": m}) for d, a, m in _rows(path)]

def total(rows: list[Row]) -> float:
    return sum(r.amount for r in rows)
```
A bad `amount` now raises in `load`, not as a `KeyError` three calls later.

## rule-group-by-subject

`total(rows)`, `by_month(rows)`, `largest(rows)` stay module functions in `ledger.py`; `smallest(rows)` joins them. The class the file earns:
```python
@dataclass(frozen=True)
class LedgerRepository:
    path: Path

    def load(self) -> tuple[Row, ...]: ...
```
It holds the path and decides how a line becomes a `Row`; a test can hand the functions rows without it.

## rule-no-pass-through

```python
def read_ledger(path: Path) -> LedgerReport:   # delete; callers call load
    return load(path)
```

## rule-split-on-the-seam

`ledger.py` imports `pydantic` for `Row` and `httpx` for `fetch_rates`: two subjects. `ledger/rows.py` keeps `Row` and `load` (imports only `pydantic`, `pathlib`); `ledger/rates.py` keeps `fetch_rates` (imports `httpx` and `Row`).

## rule-smallest-change

Asked: "include rows with an empty memo". Not this:
```python
def load(path: Path, include_empty: bool = True) -> list[Row]:
```
This: delete the `if not memo: continue` line and fix the one test that encoded the skip.
