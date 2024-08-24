import sqlite3
import os

DB_FILE = 'todos.db'

def get_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    if not os.path.exists(DB_FILE):
        db = get_db()
        db.execute('CREATE TABLE todos (id INTEGER PRIMARY KEY, title TEXT, completed BOOLEAN)')
        db.close()

def get_todos():
    db = get_db()
    todos = db.execute('SELECT * FROM todos').fetchall()
    db.close()
    return [dict(todo) for todo in todos]

def add_todo(title):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO todos (title, completed) VALUES (?, ?)', (title, False))
    todo_id = cursor.lastrowid
    db.commit()
    db.close()
    return {'id': todo_id, 'title': title, 'completed': False}

def update_todo(todo_id, completed):
    db = get_db()
    db.execute('UPDATE todos SET completed = ? WHERE id = ?', (completed, todo_id))
    db.commit()
    db.close()
    return {'id': todo_id, 'completed': completed}

def delete_todo(todo_id):
    db = get_db()
    db.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    db.commit()
    db.close()
    return {'id': todo_id}

init_db()