from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

# Modèle de données pour un Todo
class Todo(BaseModel):
    id: str
    title: str
    description: str

class TodoNoId(BaseModel):
    title: str
    description: str