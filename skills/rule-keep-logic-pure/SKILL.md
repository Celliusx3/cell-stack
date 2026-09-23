---
name: rule-keep-logic-pure
description: A body that both talks to the outside and decides something is split; the decision is a plain function beside the shell, typed in and typed out, with no framework import, and the shell is the read, the call and the write. Test the decision without the framework. From pstack's boundary-discipline and minimize-reader-load.
disable-model-invocation: true
---

# Keep logic pure

## When

A function body both talks to the outside (reads a file, a socket, the clock, a database, the DOM; a React effect; a request handler) and decides something (parses, filters, picks, scores, builds a prompt). Also when you are about to test something and find you need the framework to reach the logic: a renderer to check a sort, a running server to check a parse. It does not apply to a shell that only reads and writes with no decision in between, or to a decision that already takes typed data and returns typed data.

## Rule

The decision is a plain function beside the shell, typed in and typed out, with no framework import. The shell is the read, the call, and the write, and nothing else. Test the decision without the framework: hand it values, check what comes back.

Instead of the tempting thing: do not put an if-chain inside the effect or the handler because it is "just a few lines". Those lines are the part worth testing, and inside the shell they can only be tested through the shell.

## The test

pstack's own question: "Can this be a pure function that the shell just calls? If yes, extract it."

## Example

Before, a made-up effect in the shape this bans:

```tsx
useEffect(() => {
  listRows().then((listed) => {
    const kept = listed.filter((r) => filter === "all" || r.kind === filter);
    kept.sort((a, b) => b.date.localeCompare(a.date));
    setRows(kept);
  });
}, [filter]);
```

After: `visibleRows(listed: Row[], filter: Filter): Row[]` sits beside it and does the filter and the sort; the effect is `listRows().then((listed) => setRows(visibleRows(listed, filter)))`. `visibleRows` has a test that hands it four rows and a filter and checks the order, with no React in the file.
