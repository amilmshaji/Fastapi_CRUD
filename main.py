from fastapi import FastAPI, HTTPException

from model import Item


app = FastAPI()


items: list[Item] = [
    Item(id=1, name="foo", description="demo tem 1",stock=1),
    Item(id=2, name="bar", description="demo tem 2",stock=10),    
]

# creating API endpoint
@app.get("/")
def status() -> dict:
    return {"status":"ok","mesaage":"hello"}

#listing all the items in the list
@app.get("/items")
def get_items() -> list[Item]:
    return items

#list be id
@app.get("/items/{item_id}")
def get_item(item_id: int)-> Item:
    for item in items:
        if item.id==item_id:
            return item
    raise HTTPException(status_code=400,detail=f"Item wih id: {item_id} not found")

#adding new items    
@app.post("/items_add")
def create_item(item: Item)-> Item:
    for i in items:
        if i.id == item.id:
            raise HTTPException(status_code=400, detail=f"Item with id {item.id} already exixts")
    items.append(item)
    return item

#updating items in the list
@app.post("/items_update")
def update_item(item: Item) -> Item:
    for i in items:
        if i.id == item.id:
            i.name = item.name
            i.stock = item.stock
            i.description = item.description
            return i
    raise HTTPException(status_code=400,detail=f"Item wih id: {item.id} not found")

        
#deleting items from the list
@app.delete("/items_del/{item_id}")
def delete_item(item_id: int) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return
    raise HTTPException(status_code=400,detail=f"Item wih id: {item_id} not found")

