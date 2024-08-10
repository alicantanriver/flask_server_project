from collections import defaultdict
import sqlite3
from flask import Flask, jsonify
from flask import request
from flask import render_template
import os.path

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('to_do_list.html')

@app.route('/<username>')
def profile(username):
    
    # if username and not username[0].isupper:
    #     username = username[0].upper() + username[1:]
    # return f'My name is {username}'
    username = username.capitalize()
    return f'My name is {username}'

@app.route('/list')
def sampleList():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "test.db")
    
    con = sqlite3.connect(db_path)
    # con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    cur.execute('SELECT Name FROM Mahmut')
    rows = cur.fetchall()
    con.close()

    names = [row[0] for row in rows]

    return ", ".join(names)

@app.route('/details')
def toDo():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "todolist.db")
    
    con = sqlite3.connect(db_path)
    
    cur = con.cursor()
    cur.execute('SELECT list.name, item.name FROM list JOIN item ON (list.id=item.list_id)')
    rows = cur.fetchall()
    con.close()

    grouped_data = defaultdict(list)
    for row in rows:
        grouped_data[row[0]].append(row[1])

    # Format the grouped data as a string
    result_string = ''.join(
    [f"<h3>{key}</h3><ul>" + ''.join([f"<li>{item}</li>" for item in values]) + "</ul>" for key, values in grouped_data.items()]
)

    return result_string


if __name__ == '__main__':
    app.run(debug=True)