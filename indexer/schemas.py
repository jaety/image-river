import sqlite3
from contextlib import contextmanager

@contextmanager
def sqlite_cursor(fn):
    conn = sqlite3.connect(fn)
    c = conn.cursor()
    yield c
    conn.commit()
    conn.close()

def sqlite_execute(fn, *cmds):
    with sqlite_cursor(fn) as c:
        for cmd in cmds:
            c.execute(cmd)


def create(fn):
    sqlite_execute(fn,
        "CREATE TABLE system_id (name text, id text)",
        "CREATE TABLE image_file (system_id text, path text, id text)",
        "CREATE TABLE image_metadata (image_id text, width integer, height integer)"
    )

def clean(fn):
    sqlite_execute(fn,
        "DROP TABLE system_id",
        "DROP TABLE image_file",
        "DROP TABLE image_metadata"
    )
