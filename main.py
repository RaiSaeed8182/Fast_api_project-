from fastapi import FastAPI 
app=FastAPI()

@app.get("/")
def read_root():
    return {"messgae": "Hello world "}
@app.get("/helth")
def health_checker():
 return {"message":"helath","service":"medicare_pro_project"}

 