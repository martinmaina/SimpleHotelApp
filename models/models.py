import sqlite3


def database():
    return sqlite3.connect('message.db')
def dropTb():
        con = database()
        con.execute('DROP TABLE  IF EXISTS messageTable')
        con.commit()
        con.close()

def createTb():
        con = database()
        con.execute('CREATE TABLE  IF NOT EXISTS messageTable (jin text, email text, mess text)')
        con.commit()
        con.close()


def addVerse(jina, mail, arafa):
        con = database()
        # c = con.cursor()
        con.execute('INSERT INTO messageTable (jin, email,  mess) VALUES (? , ?, ?)', (jina, mail, arafa) )
        con.commit()
        con.close()