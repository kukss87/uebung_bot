import sqlite3 as sq


def create_db():
    conn = sq.connect('bot.db')
    cur = conn.cursor()
    with open('sql_db.sql', 'r') as f:
        cur.executescript(f.read())
    conn.commit()
    conn.close()


def get_db():
    """Соединение с БД, если оно не установлено"""
    conn = sq.connect('lessons.db')
    return conn


def connect_db():
    conn = sq.connect(database='users.db')
    conn.row_factory = sq.Row
    return conn


create_db()
get_db()
connect_db()


class Database:
    def __init__(self, db):
        self.connection = sq.connect(db)
        self.cursor = db.cursor()

