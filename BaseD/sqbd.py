import sqlite3 as sq
from sqlite3 import Cursor


async def db_connect() -> None:
    db = sq.connect('./Users.db')
    cur = db.cursor()


async def get_ank():
    db = sq.connect('./Users.db')
    cur = db.cursor()
    ank = cur.execute("SELECT * FROM Users_ank").fetchall()

    return ank


async def add_new_ank(FIO, Educat, Profes, Experience, Qualit, Languag, Info, Works, Contacts):
    db = sq.connect('./Users.db')
    cur = db.cursor()
    cur.execute("INSERT INTO Users_ank VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('', FIO, Educat, Profes, Experience, Qualit, Languag, Info, Works, Contacts))
    db.commit()
