from typing import final

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message":"this is first default route"}



# Single value parameter
# http://127.0.0.1:8000/items/36
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"This is fetched from the url parameter": item_id}


# Multi value prameter
# http://127.0.0.1:8000/items/?item_id=35&name=jack
@app.get("/items/")
def read_multi_item(item_id: int, name:str=None):
    return {"This is fetched from the url parameter where item_id": item_id, "name":name}


# Using Pydantic Models for validation and json conversion auto
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}

# Dependency Injection
from fastapi import Depends

class Database:
    def __init__(self):
        self.connection = "Database connection initiated"
    def get_data(self):
        return "Data from the database"
def get_db():
    db = Database()
    try:
        yield db
    finally:
        pass

@app.get("/data")
async def read_data(db: Database= Depends(get_db)):
    return {"data": db.get_data()}

# Path Operations
@app.get("/items/{item_id}",
         summary="Get an item",
         description="Retrieve a specific item by its ID.",
         tags=["Items"])
def read_item(item_id: int):
    return {"item_id": item_id}




