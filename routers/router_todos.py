from fastapi import APIRouter, Depends, HTTPException, status
import uuid
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from classes.models import Todo, TodoNoId
import uuid


router= APIRouter(
    prefix='/todos',
    tags=["todos"]
)



# Base de données de tous les todos
todos_db = []


# Opération Read (lister tous les todos)
@router.get("", response_model=list[Todo])
def read_todos():
    return todos_db


# Opération Create (ajouter un nouveau todo)
@router.post("", response_model=Todo, status_code=201)
def create_todo(todo: TodoNoId):
    # Générer un UUID
    todo_id = str(uuid.uuid4())
    # Créer le todo avec l'ID généré
    todo_data = todo.dict()
    todo_data["id"] = todo_id
    new_todo = Todo(**todo_data)
    todos_db.append(new_todo)
    return new_todo

# Opération Read (lire un todo spécifique)
@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: str):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Opération Update (mettre à jour un todo spécifique)
@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo: Todo):
    for index, existing_todo in enumerate(todos_db):
        if existing_todo.id == todo_id:
            todo.id = existing_todo.id
            todos_db[index] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Opération Delete (supprimer un todo spécifique)
@router.delete("/{todo_id}", response_model=Todo)
def delete_todo(todo_id: str):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(index)
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")