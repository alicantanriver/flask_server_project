import os
import sqlite3
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_data(id: int):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "todolist.db")
    
    con = sqlite3.connect(db_path)
    
    cur = con.cursor()
    cur.execute(f'SELECT name FROM item WHERE item.list_id = {id}')
    rows = cur.fetchall()
    con.close()
    tasks = [row[0] for row in rows]
    return tasks

def add_data(id: int, itemName: str):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "todolist.db")
    
    con = sqlite3.connect(db_path)
    
    cur = con.cursor()
    # Parameterized query for insertion
    query = '''
    INSERT INTO item (id, list_id, name, orderNo) 
    VALUES (?, ?, ?, ?);
    '''

    # Generate random numbers
    random_order_no = random.randint(5009, 9999)
    random_item_id = random.randint(110, 999)
    
    # Execute the query with parameters
    cur.execute(query, (random_item_id, id, itemName, random_order_no))

    con.commit()
    con.close()

home_list = get_data(1)
work_list = get_data(2)
groceries_list = get_data(3)

@app.route('/')
def index():
    return render_template('task_template.html', 
                           home_list=home_list, 
                           work_list=work_list, 
                           groceries_list=groceries_list)

@app.route('/home')
def home():
    return render_template('home.html', 
                           home_list=home_list)

@app.route('/work')
def work():
    return render_template('work.html', 
                           work_list=work_list)

@app.route('/groceries')
def groceries():
    return render_template('groceries.html', 
                           groceries_list=groceries_list)

@app.route('/add_home_task', methods=['POST'])
def add_home_task():
    new_task = request.form.get('newtask')
    if new_task:
        home_list.append(new_task)
        add_data(1, new_task)
    return redirect(url_for('home'))


@app.route('/add_work_task', methods=['POST'])
def add_work_task():
    new_task = request.form.get('newtask')
    if new_task:
        work_list.append(new_task)
        add_data(2, new_task)
    return redirect(url_for('work'))

@app.route('/add_groceries_task', methods=['POST'])
def add_groceries_task():
    new_task = request.form.get('newtask')
    if new_task:
        groceries_list.append(new_task)
        add_data(3, new_task)
    return redirect(url_for('groceries'))

if __name__ == "__main__":
    app.run(debug=True)

