from fastapi import FastAPI 
from pydantic import BaseModel 
app=FastAPI()

@app.get("/")
def read_root():
    return {"messgae": "Hello world "}
@app.get("/helth")
def health_checker():
 return {"message":"helath","service":"medicare_pro_project"}



def calculate_consultation_fee(hours:float , rate_per_hour: float)-> float:
    return hours*rate_per_hour


print(calculate_consultation_fee(10.0,6.5))



class patient:
   def  __init__(self,name:str,age:int):
    self.name=name 
    self.age = age 

p1=patient(name="Ali",age=5)
p2=patient(name="Saeed",age=10)
patients:list[patient]=[p1,p2]

def get_patients()->list[patient]:
    return patients


class Doctor(BaseModel):
    name:str 
    age:int
    fee:float 

d1 = Doctor(name="saeed",age=13,fee=255.0)
print(d1)
d2 = Doctor(name=123,age="13",fee=255.0)
print(d2)