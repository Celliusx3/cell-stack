# Smallest change

The minimum code that solves the asked problem, and every changed line traces to the request. No speculative abstraction, no option nobody asked for. From pstack's laziness-protocol and subtract-before-you-add, and the KISS + YAGNI rule most projects state.

## When

Any code change: a feature, a fix, a refactor. Sizing a diff. The moment you are tempted to add a layer, a flag, a helper, a base class, or a "while I'm here" cleanup. It does not apply to deleting, because subtraction is always in scope.

## Rule

Write the minimum code that solves the problem that was asked. Make every changed line traceable to the request. Do not build for a caller that does not exist yet. Three similar paths is fine. Extract at about five, when the shape has genuinely converged.

A stated house rule (typed boundaries, fail closed, a file cap) outranks diff size. A smaller diff that breaks one is not a saving.

Instead of the tempting thing, when you see a second use coming, write it down in the reply as a follow-up. Leave the code as it is.

## The test

Read the diff hunk by hunk. For each, name the sentence in the request that caused it. A hunk with no sentence comes out.
