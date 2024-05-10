from fastapi import APIRouter, Depends, HTTPException, status
import uuid
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from classes.models import Todo, TodoNoId
import uuid
from database.firebase import db
from routers.router_auth import get_current_user


router= APIRouter(
    prefix='/todos',
    tags=["todos"]
)



# Base de données de tous les todos
todos_db = []


# Opération Read (lister tous les todos)
@router.get("", response_model=list[Todo])
async def read_todos(userData: int = Depends(get_current_user)):
      fireBaseobject = db.child("users").child(userData['uid']).child('todos').get(userData['idToken']).val()
      if fireBaseobject == None : return []
      resultArray = [value for value in fireBaseobject.values()]
      return resultArray


# Opération Create (ajouter un nouveau todo)
@router.post("", response_model=Todo, status_code=201)
async def create_to_do(todo: TodoNoId, userData: int = Depends(get_current_user)):
      # Générer un UUID
      todo_id = str(uuid.uuid4())
      newTodo = Todo(id=str(todo_id), title=todo.title, description=todo.description)
      # Enregistrer le todo dans Firestore
      db.child('users').child(userData['uid']).child("todos").child(str(todo_id)).set(newTodo.model_dump(), userData['idToken'])
      return newTodo

# Opération Read (lire un todo spécifique)
@router.get("/{todo_id}", response_model=Todo)
async def get_by_id(todo_id: str, userData: dict = Depends(get_current_user)):
    todoById = db.child("users").child(userData['uid']).child('todos').child(str(todo_id)).get(userData['idToken']).val()
    
    if todoById is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = Todo(**todoById)
    return todo

# Opération Update (mettre à jour un todo spécifique)
@router.patch("/{todo_id}", status_code=204)
async def update_todo(todo_id: str, todoUpdated: TodoNoId, userData: int = Depends(get_current_user)):
    
    firebaseObject = db.child("users").child(userData['uid']).child('todos').child(todo_id).get(userData['idToken']).val()
    if firebaseObject is not None:
        todoUpdated = Todo(id=todo_id, **todoUpdated.model_dump())
        return db.child("users").child(userData['uid']).child('todos').child(todo_id).update(todoUpdated.model_dump(), userData['idToken'] )
    raise HTTPException(status_code= 404, detail="Todo not found")

# Opération Delete (supprimer un todo spécifique)
@router.delete("/{todo_id}", status_code=204)
async def delete_todo(todo_id: str, userData: int = Depends(get_current_user)):
    todoDelete = db.child("users").child(userData['uid']).child('todos').child(todo_id).get(userData['idToken']).val()
    if todoDelete is None:
      raise HTTPException(status_code=404, detail="Todo not found")
    # Delete the Todo data
    db.child("users").child(userData['uid']).child('todos').child(str(todo_id)).remove(userData['idToken'])
    return None