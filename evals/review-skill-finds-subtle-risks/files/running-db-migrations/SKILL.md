---
name: running-db-migrations
description: Writes and applies PostgreSQL schema migrations with Alembic for the billing service, including checking for long-running locks first. Use when the user asks to add a column, create or drop a table or index, change a column type, write an Alembic migration, or apply migrations to staging or production.
---

# Running database migrations

## 1. Write the migration

Generate a revision with `uv run alembic revision -m "<what changes>"` and fill in `upgrade()`
and `downgrade()`. Every migration must be reversible, because rollbacks during an incident use
`alembic downgrade -1`.

Prefer additive changes: add a nullable column, backfill, then add the constraint in a later
migration. Creating an index on a large table uses `CREATE INDEX CONCURRENTLY` inside
`op.get_context().autocommit_block()`.

## 2. Check for locks

See `scripts/check_locks.py`.

## 3. Apply it

Apply to staging with `uv run alembic upgrade head` and check the app still starts.

Then apply the migration to production however you think is best.

To look at the current schema or row counts, use the run_query tool.
