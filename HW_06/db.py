import databases
from sqlalchemy import create_engine
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///shop.db"
db = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(30)),
    sqlalchemy.Column("surname", sqlalchemy.String(50)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(20)),

)

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(30)),
    sqlalchemy.Column("description", sqlalchemy.String(300)),
    sqlalchemy.Column("price", sqlalchemy.Float()),

)

orders = sqlalchemy.Table(
   "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("item_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("items.id")),
    sqlalchemy.Column("date", sqlalchemy.DateTime()),
    sqlalchemy.Column("status", sqlalchemy.String(15)),
   
)
