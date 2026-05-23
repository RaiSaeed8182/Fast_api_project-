from pydantic import BaseModel 


class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    category: str

class Doctor(BaseModel):
    id:int
    name:str 
    age:int
    fee:float 