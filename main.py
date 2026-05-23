from fastapi import FastAPI
from routes import doctors,menu

app = FastAPI(title="Food Ai")

## Routers add karo or connect karo 

app.include_router(doctors.routers)
app.include_router(menu.routers)

@app.get("/")
def root():
    return {"message": "Welcome tp Food Ai "}