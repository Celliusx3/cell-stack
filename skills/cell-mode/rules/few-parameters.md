# Few parameters

A function takes at most four parameters; a fifth means some of them travel together and become one typed value. From the person's call on 2026-10-11, after a helper that sent a saved key took five arguments, three of which were one saved secret.

## When

Writing or changing a function, a method, a constructor or a route handler. Reading a call site whose arguments only make sense by position. `self` and `cls` do not count; keyword-only parameters do.

## Rule

Four parameters at most. A fifth means some of them always arrive together or come from one object: pass that object, or name the group as one typed value (**rule-typed-boundaries**) and pass it. A composition root that wires many services is no exception; the services it passes on are a group.

Instead of the tempting thing: do not hide the extra ones in a loose options map, `**kwargs`, or a default nobody sets. The count drops and the coupling stays.

## The test

Count the parameters. At five or more, ask which of them every caller takes from the same place. That group is the missing type.
