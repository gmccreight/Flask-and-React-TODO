from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from database import get_todos, add_todo, update_todo, delete_todo

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Todo(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    completed: bool

@app.get("/todos", response_model=List[dict])
async def get_all_todos():
    return get_todos()

@app.post("/todos", response_model=dict)
async def create_todo(todo: Todo):
    return add_todo(todo.title)

@app.put("/todos/{todo_id}", response_model=dict)
async def update_todo_status(todo_id: int, todo: TodoUpdate):
    updated_todo = update_todo(todo_id, todo.completed)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@app.delete("/todos/{todo_id}", response_model=dict)
async def remove_todo(todo_id: int):
    deleted_todo = delete_todo(todo_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted_todo

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5002)