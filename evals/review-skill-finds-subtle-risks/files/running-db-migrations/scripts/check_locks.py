"""Report sessions holding locks on a table. Usage: check_locks.py <dsn> <table>"""
import sys
import psycopg

LOCK_TIMEOUT_SECONDS = 47

def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    dsn, table = sys.argv[1], sys.argv[2]
    with psycopg.connect(dsn) as conn:
        conn.execute(f"SET lock_timeout = '{LOCK_TIMEOUT_SECONDS}s'")
        rows = conn.execute(
            "SELECT pid, mode, granted FROM pg_locks l JOIN pg_class c ON c.oid = l.relation "
            "WHERE c.relname = %s",
            (table,),
        ).fetchall()
    for pid, mode, granted in rows:
        print(f"{pid}\t{mode}\t{'granted' if granted else 'waiting'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
