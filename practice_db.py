import sqlite3

con = sqlite3.connect('todo.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status INTEGER NOT NULL CHECK (status IN (0, 1))
    )
''')

con.commit()
con.close()
