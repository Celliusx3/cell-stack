# Name for the reader

A name tells someone who has not opened the thing what is inside it or what comes back: a folder or a file is named for its subject, a class for what an instance is, a function for what the caller gets back or what it does. From a correction on 2026-09-24, when a service's `due`, `refusal` and `reduce` became a question, a reason and a plain verb, and the person's review on 2026-10-17 of a project whose one-word functions (`apply`, `repair`, `drained`) each needed their docstring to be read.

## When

Naming or renaming a folder, a file, a class, a function, a method or a test. Reading a name you understood only after opening it: a call site that needs the docstring, a file you opened to learn what it holds. The signals: a verb that fits anything (`handle`, `process`, `apply`, `run`, `do`, `manage`); a bare verb whose object is nowhere in the call; a bare adjective or past participle on a function that acts (`due`, `ready`, `drained`, `settled`); a bare noun that hides what comes back (`refusal`, `render`, `report`); a catch-all (`utils`, `helpers`, `common`, `misc`, `Manager`, `Helper`, `Processor`); a name that repeats its folder.

It does not apply to a name the framework or the project's own rules fix: a package's init file, a router's page file, a test runner's prefix, an entry file every package in the project shares.

## Rule

1. A folder is named for the subject every file in it shares, in the project's words. Not a catch-all, and not a layer word (`adapters/`, `repositories/`) standing in for the subject.
2. A file is named for its one subject in its folder's words. It does not repeat the folder (`billing/invoice.py`, not `billing/billing_invoice.py`), and it is never `utils`, `helpers`, or a verb joined to a layer (`edit_tools`).
3. A class is named for what an instance is: the plain noun for a data shape (`Invoice`), the subject plus its role for one that holds state or hides a decision (`OrderRepository`, `MailSender`). `Manager`, `Helper` and `Processor` never stand in for the role unless the project already uses the word for that concept. An adjective or a participle is not a class name (`Parsed`), and a case of a union is a noun too: `Approval | Denial`, not `Approved | Denied`.
4. A function is named for what the caller gets back:
   1. A yes or no reads as a question: `should_close`, `is_empty`, `has_access`.
   2. A value is named for the value, and adds its kind when the type does not show it: `refusal_reason`, `unposted_ids`, `timeout_seconds`. A past participle names a value only when it is the input changed: `sorted(rows)`.
   3. An action is the verb and its object: `run_command`, `send_invoice`. The bare verb is enough only when the call already names the object: `ledger.close(month)`, `invoice.send()`. A function imported by name loses its module at the call, so it carries its object itself.
5. A constant is named for what it holds: the string `"__"` between a server and a tool name is `NAMESPACE_SEPARATOR`, not `NAMESPACE`, and a constant holding a name is that name (`GET_LOCATION = "get_location"`, not `LOCATION`).
6. A test is named for the promise it checks: `test_a_failed_summary_changes_nothing`, not `test_summary`, and not the name of the function it calls.

Before naming a function, ask whether it should exist. When it only picks one field for each case of a union, give every case that field and delete the function: a failure's `content`, beside a success's, rather than a `blocks_of(outcome)` that builds one of them. A name copied from a sibling's pattern fits only when the function does the same kind of thing: `text_of(blocks)` reads text that is already there, so a function that builds new text for one case is not an `_of`.

Instead of the tempting thing: do not keep a short name and explain it in the docstring. If the docstring is what makes the call readable, the docstring's words belong in the name.

## The test

Write each candidate into its real call site and read the line out loud, without opening the path or the function. Offer the person call sites, not bare names. `billing/invoice.py` and `if ledger.should_close(month): ledger.close(month)` say what is inside and what comes back. `if ledger.due(month): ledger.reduce(month)` needs the docstring. If it needs the docstring, rename it.
