from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/todo_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    completed: bool

class NoteCreate(BaseModel):
    body: str

class NoteResponse(BaseModel):
    id: int
    body: str
    created_at: datetime

    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3002", "http://127.0.0.1:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Todo endpoints
@app.get("/todos", response_model=List[dict])
async def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return [{"id": todo.id, "title": todo.title, "completed": todo.completed} for todo in todos]

@app.post("/todos", response_model=dict)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return {"id": db_todo.id, "title": db_todo.title, "completed": db_todo.completed}

@app.put("/todos/{todo_id}", response_model=dict)
async def update_todo_status(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.completed = todo.completed
    db.commit()
    return {"id": db_todo.id, "title": db_todo.title, "completed": db_todo.completed}

@app.delete("/todos/{todo_id}", response_model=dict)
async def remove_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"id": db_todo.id, "title": db_todo.title, "completed": db_todo.completed}

# Note endpoints
@app.post("/notes", response_model=NoteResponse)
async def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(body=note.body)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes", response_model=List[NoteResponse])
async def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

@app.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5002)