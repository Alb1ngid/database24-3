# crud create read update delete

import sqlite3

bd = sqlite3.connect('26_3.db')

c = bd.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
title text,
full text,
view integer,
avtor text
)

''')
# c.execute("INSERT INTO user VALUES ('ЭТО СТАТЬЯ','',100,'BEKA')")
# c.execute("INSERT INTO user VALUES ('ЭТО СТАТЬЯ','',100,'BEKA')")
c.execute("DELETE FROM user WHERE rowid > 2")
c.execute("UPDATE user SET avtor = 'non' WHERE title = 'SFD'")
c.execute("SELECT * FROM user WHERE avtor <> 'BEKA'")
c.execute("SELECT * FROM user ORDER BY title DESC ")
# c.execute("SELECT avtor FROM user")
# print(c.fetchall())
# print(c.fetchone())
# print(c.fetchmany(2))

items=c.fetchall()
for el in items:
    print(el)

bd.commit()
bd.close()
