import sqlite3 as sq
from data_processing import process_data


def create_db():
    conn = sq.connect('bot.db')
    cur = conn.cursor()
    with open('sql_db.sql', 'r') as f:
        cur.executescript(f.read())
    conn.commit()
    conn.close()


def get_db(db='bot.db'):
    """Соединение с БД, если оно не установлено"""
    conn = sq.connect(db)
    return conn


class Database:
    def __init__(self, db='bot.db'):
        self.conn = sq.connect(db)
        self.cur = self.conn.cursor()

    def create_table(self, tablename):
        """Создание таблицы в БД"""
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {tablename} (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                      task TEXT,
                                                                      correct_answer TEXT)""")
        conn.commit()
        conn.close()
        return f'Таблица {tablename} создана'

    @staticmethod
    def insert_data(tablename, filename):
        """Добавление данных в БД"""
        conn = get_db()
        cur = conn.cursor()
        data = process_data(filename)
        cur.executemany(f"""INSERT INTO {tablename} (task, correct_answer) VALUES (?, ?)""", data)
        conn.commit()
        conn.close()

    @staticmethod
    def get_data(tablename):
        """Получение данных из БД"""
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"""SELECT task, correct_answer FROM {tablename}""")
        rows = cur.fetchall()
        conn.close()
        return rows

    def get_random_task(self, tablename):
        """Выбор случайной задачи из БД"""
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"""SELECT task, correct_answer FROM {tablename} ORDER BY RANDOM() LIMIT 1""")
        row = cur.fetchone()
        conn.close()
        return row


# dbase = Database()
# dbase.create_table('perfekt')
# dbase.insert_data(tablename='perfekt', filename='perfekt.txt')
# # print(dbase.get_data(tablename='perfekt'))
# print(dbase.get_random_task(tablename='perfekt'))
