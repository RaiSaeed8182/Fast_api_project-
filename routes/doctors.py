from fastapi import APIRouter, HTTPException
from model import Doctor
from sys import prefix

routers = APIRouter(
    prefix="/doctor",
    tags=["doctors"]
)

data_list=[]

@routers.post("/",status_code=201)
async def create_data(doctor:Doctor): 
     data_list.append(doctor)
     return {"message": "Doctor added successfully", "doctor": doctor}

@routers.get("/")
async def get_all_doctor_data(min_age: int=0):
    filter_doctors=[]
    for doctor in data_list: 
        if doctor.age >= min_age: 
            filter_doctors.append(doctor.age)
    return filter_doctors

@routers.put("/{doctor_id}")
async def update_doctor(doctor_id: int, update_doctor:Doctor): 
    for index,doctor in enumerate (data_list): 
        if doctor.id == doctor_id : 
            data_list[index]=update_doctor
            return {"message":"The data is update Know"}
    raise HTTPException(status_code=404, detail="Doctor not Found")


@routers.delete("/{id}")
async def delete_data(id:int): 
    for  doctor  in data_list : 
        if doctor.id == id : 
            data_list.pop(doctor.id)
            return {"message":"The data is delete successfully"}
    raise HTTPException(status_code=404, detail="Data not found ")
