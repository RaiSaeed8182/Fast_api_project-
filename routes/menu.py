from sys import prefix
from fastapi import APIRouter, HTTPException
from model import MenuItem 

routers=APIRouter(
    prefix="/menu",
    tags=["Menu"]
)

all_menu=[]
@routers.post("/", status_code=201)
def create_menu(item_menu:MenuItem): 
   all_menu.append(item_menu)
   return {"message":"item added successfully","menu":item_menu}

@routers.get("/")
def get_all_menu(max_price:int=999): 
    fillter_price=[]
    for item in all_menu: 
        if item.price <= max_price: 
            fillter_price.append(item.price)
    return fillter_price

@routers.put("/{item_id}")
def update_item(item_id:int, update_data:MenuItem): 
    for index, item in enumerate(all_menu):
        if item.id == item_id : 
            all_menu[index] = update_data
            return {"message":"The update successfully"}
    raise HTTPException(status_code=404, detail="The data is not found ")

@routers.delete("/{item_id}")
def delete_data(item_id:int): 
    for item in get_all_menu: 
        if item.id == item_id: 
           get_all_menu.pop(item.id)
           return {"message":"Data is Delete"}
    raise HTTPException(status_code=404, detail="The data is not found ")

 