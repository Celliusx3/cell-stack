# Keep logic pure

A body that both talks to the outside and decides something is split. The decision is a plain function beside the shell, typed in and typed out, with no framework import. The shell is the read, the call and the write. Test the decision without the framework. From pstack's boundary-discipline and minimize-reader-load.

## When

A function body both talks to the outside and decides something. Talking to the outside is a read of a file, a socket, the clock, a database or the DOM. A React effect and a request handler talk to the outside too. Deciding is parsing, filtering, picking, scoring, or building a prompt. It also applies when a test needs the framework to reach the logic. Examples are a renderer to check a sort, or a running server to check a parse.

It does not apply to a shell that only reads and writes, with no decision in between. It also does not apply to a decision that already takes typed data and returns typed data.

## Rule

The decision is a plain function beside the shell, typed in and typed out, with no framework import. The shell is the read, the call, and the write, and nothing else. Test the decision without the framework. Hand it values, and check what comes back.

Instead of the tempting thing, do not put an if-chain inside the effect or the handler because it is "just a few lines". Those lines are the part worth testing. Inside the shell, they can only be tested through the shell.

## The test

pstack's own question: "Can this be a pure function that the shell just calls? If yes, extract it."
