## Backend

This is the backend for the Todo application, built with FastAPI

### Prerequisites

- Python 3.7+

### Setup

The `./run_in_env` script will create a virtual environment, install the dependencies, and run the application.

The server will start on `http://localhost:5002`.

## API Endpoints

- GET /todos: Retrieve all todos
- POST /todos: Create a new todo
- PUT /todos/{todo_id}: Update a todo's status
- DELETE /todos/{todo_id}: Delete a todo