from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

# Modèle de données pour un Todo
class Todo(BaseModel):
    id: str
    title: str
    description: str

class TodoNew(BaseModel):
    title: str
    description: str

# Initialiser FastAPI
app = FastAPI(
  title="My Todos API",
  description= "Manage your todos with this simple api",
  docs_url='/'
)

# Base de données de tous les todos
todos_db = []

# Opération Create (ajouter un nouveau todo)
@app.post("/todos/", response_model=Todo, status_code=201)
def create_todo(todo: TodoNew):
    # Générer un UUID
    todo_id = str(uuid.uuid4())
    # Créer le todo avec l'ID généré
    todo_data = todo.dict()
    todo_data["id"] = todo_id
    new_todo = Todo(**todo_data)
    todos_db.append(new_todo)
    return new_todo

# Opération Read (lister tous les todos)
@app.get("/todos/", response_model=List[Todo])
def read_todos():
    return todos_db

# Opération Read (lire un todo spécifique)
@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: str):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Opération Update (mettre à jour un todo spécifique)
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo: Todo):
    for index, existing_todo in enumerate(todos_db):
        if existing_todo.id == todo_id:
            todo.id = existing_todo.id
            todos_db[index] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Opération Delete (supprimer un todo spécifique)
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: str):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(index)
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")