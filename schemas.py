# schemas.py
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    title: str
    description: str

class TodoAll(TodoBase):
    id: int
    title: str
    description: str

class TodoRead(TodoBase):
    id: int

    class Config:
        orm_mode = True
