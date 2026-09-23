# TypeScript patterns

One before / after per rule.

## rule-typed-boundaries

Before:
```ts
async function load(url: string): Promise<Record<string, any>[]> {
  return (await fetch(url)).json();
}
function total(rows: Record<string, any>[]): number {
  return rows.reduce((sum, r) => sum + r.amount, 0);
}
```

After:
```ts
const Row = z.object({ date: z.string(), amount: z.number(), memo: z.string() });
type Row = z.infer<typeof Row>;

async function load(url: string): Promise<Row[]> {
  return z.array(Row).parse(await (await fetch(url)).json());
}
function total(rows: Row[]): number {
  return rows.reduce((sum, r) => sum + r.amount, 0);
}
```
A bad `amount` throws in `load`, not as `NaN` three calls later.

## rule-group-by-subject

`total(rows)`, `byMonth(rows)`, `largest(rows)` stay exported functions in `ledger.ts`; `smallest(rows)` joins them. The class the file earns:
```ts
class LedgerRepository {
  constructor(private readonly url: string) {}
  async load(): Promise<readonly Row[]> { ... }
}
```
It holds the url and decides how a line becomes a `Row`; a test can hand the functions rows without it.

## rule-no-pass-through

```ts
export const readLedger = (url: string) => load(url);   // delete; callers call load
```

## rule-split-on-the-seam

`ledger.ts` imports `zod` for `Row` and `react` for `useLedger`: two subjects. `ledger/rows.ts` keeps `Row` and `load`; `ledger/useLedger.ts` keeps the hook and imports `Row`.

## rule-smallest-change

Asked: "include rows with an empty memo". Not `load(url, { includeEmpty = true } = {})`. Delete the `if (!r.memo) continue;` line and fix the one test that encoded the skip.

## rule-keep-logic-pure

Before:
```tsx
useEffect(() => {
  load(url).then((rows) => {
    const kept = rows.filter((r) => r.date.startsWith(month) && r.amount !== 0);
    setRows(kept.sort((a, b) => b.date.localeCompare(a.date)));
  });
}, [url, month]);
```

After:
```tsx
export function visibleRows(rows: readonly Row[], month: string): Row[] {
  return rows
    .filter((r) => r.date.startsWith(month) && r.amount !== 0)
    .sort((a, b) => b.date.localeCompare(a.date));
}

useEffect(() => { load(url).then(setRows); }, [url]);
const visible = useMemo(() => visibleRows(rows, month), [rows, month]);
```
`visibleRows` has a test that passes three rows and reads the array back; no renderer, and the month filter is no longer a refetch.

## rule-strengthen-the-type

Before:
```ts
function largest(rows: Row[]): Row {
  if (rows.length === 0) throw new Error("should never happen");
  return rows.reduce((a, b) => (b.amount > a.amount ? b : a));
}
```

After:
```ts
type NonEmpty<T> = [T, ...T[]];

function largest(rows: NonEmpty<Row>): Row {
  return rows.reduce((a, b) => (b.amount > a.amount ? b : a));
}
```
`total(rows: Row[])` keeps the plain type, since the sum of nothing is 0; only `load` decides whether the response was empty.
