# from flask import Flask, g
# import sqlite3

# app = Flask(__name__)

# # Configure the database
# DATABASE = 'C:/SQLiteStudio/test.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# @app.route('/')
# def index():
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM Items")
#     results = cursor.fetchall()
#     return str(results)

# if __name__ == '__main__':
#     app.run(debug=True)

import sqlite3

import click
from flask import Flask, current_app, g

app = Flask(__name__)
DATABASE = 'C:/SQLiteStudio/test.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config[DATABASE],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Products")
    results = cursor.fetchall()
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)