import sqlite3 as sq


def create_db():
    conn = sq.connect('lessons2.db')
    cur = conn.cursor()
    with open('sql_db.sql', 'r') as f:
        cur.executescript(f.read())
    conn.commit()
    conn.close()


def connect_db():
    conn = sq.connect(database='lessons.db')
    conn.row_factory = sq.Row
    return conn


connect_db()
create_db()


class Database:
    def __init__(self, db):
        self.connection = sq.connect(db)
        self.cursor = db.cursor()

