from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_todos, add_todo, update_todo, delete_todo

app = Flask(__name__)
CORS(app)

@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(get_todos())

@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.json
    return jsonify(add_todo(todo['title']))

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo_status(todo_id):
    todo = request.json
    return jsonify(update_todo(todo_id, todo['completed']))

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def remove_todo(todo_id):
    return jsonify(delete_todo(todo_id))

if __name__ == '__main__':
    app.run(debug=True)