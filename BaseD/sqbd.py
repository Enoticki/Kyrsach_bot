import sqlite3 as sq


async def db_connect() -> None:
    db = sq.connect('../Users.db')
    cur = db.cursor()


async def get_ank():
    db = sq.connect('./Users.db')
    cur = db.cursor()
    ank = cur.execute("SELECT * FROM Users_ank").fetchall()

    return ank


async def get_adm():

    db = sq.connect('./Users.db')
    cur = db.cursor()
    adm = cur.execute("SELECT * FROM admin").fetchall()

    return adm
