from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    con = sqlite3.connect('todo.db')
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def index():
    con = get_db_connection()
    tasks = con.execute('SELECT * FROM tasks').fetchall()
    con.close()

    # Convert each row to a dictionary, including converting status to boolean for better clarity in JSON
    tasks_list = [dict(id=task['id'], task=task['task'], status=bool(task['status'])) for task in tasks]
    return jsonify(tasks=tasks_list)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    status = 0  # Default status is 0 (not complete)

    con = get_db_connection()
    con.execute('INSERT INTO tasks (task, status) VALUES (?, ?)', (task, status))
    con.commit()
    con.close()
    
    return jsonify(message="Task added successfully"), 201

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    status = request.form['status']

    # Convert the status to an integer (0 or 1) if it's passed as a string
    status = int(status)

    con = get_db_connection()
    con.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
    con.commit()
    con.close()
    
    return jsonify(message="Task updated successfully"), 200

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    con = get_db_connection()
    con.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    con.commit()
    con.close()
    
    return jsonify(message="Task deleted successfully"), 200

if __name__ == '__main__':
    app.run(debug=True)

