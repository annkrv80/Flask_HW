from datetime import date
from pydantic import BaseModel, Field

class UserIn(BaseModel):
    name: str = Field(max_length=30)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=128)
    password: str = Field(max_length=20)


class User(BaseModel):
    id: int
    name: str = Field(max_length=30)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=128)
    password: str = Field(max_length=20)

class ItemIn(BaseModel):
    name: str = Field(max_length=30)
    description: str = Field(max_length=300)
    price: float 
   
class Item(BaseModel):
    id: int
    name: str = Field(max_length=30)
    description: str = Field(max_length=300)
    price: float 

class OrderIn(BaseModel):
    user_id: int
    item_id : int 
    date : date
    status: str = Field(max_length=15)
   
class Order(BaseModel):
    id: int
    user_id: int
    item_id : int 
    date : date
    status: str = Field(max_length=15)

