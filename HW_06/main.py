
from typing import List
from db import *
from sqlalchemy import create_engine
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy.orm import sessionmaker, relationship
from models import *

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name,surname=user.surname, email=user.email, password=user.password)
    last_record_id = await db.execute(query)
    return {**user.dict(), "id": last_record_id}

@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await db.fetch_all(query)

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id ==
    user_id).values(**new_user.dict())
    await db.execute(query)
    return {**new_user.dict(), "id": user_id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {'message': 'User deleted'}


@app.post("/items/", response_model=Item)
async def create_item(item: ItemIn):
    query = items.insert().values(name=item.name, description=item.description, price=item.price )
    last_record_id = await db.execute(query)
    return {**item.dict(), "id": last_record_id}   

@app.get("/items/", response_model=List[Item])
async def read_items():
    query = items.select()
    return await db.fetch_all(query) 

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await db.fetch_one(query)

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, new_item: ItemIn):
    query = items.update().where(items.c.id == item_id).values(**new_item.dict())
    await db.execute(query)
    return {**new_item.dict(), "id": item_id}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await db.execute(query)
    return {'message': 'Item deleted'}

@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, item_id=order.item_id, date=order.date, status = order.status)
    last_record_id = await db.execute(query)
    return {**order.dict(), "id": last_record_id}  

@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await db.fetch_all(query)

@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await db.fetch_one(query)

@app.put("/orders/{oreder_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await db.execute(query)
    return {**new_order.dict(), "id": order_id}

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {'message': 'Order deleted'}