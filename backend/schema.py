# schema.py
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    age: int
    phone_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
