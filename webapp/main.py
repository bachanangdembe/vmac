from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB = []

class UserLocation(BaseModel):
    name: str
    email: str
    phone: str
    latitude: float
    longitude: float
    timestamp: str

@app.post("/save")
def save_user(data: UserLocation):
    DB.append(data.dict())
    return {"status": "saved"}

@app.get("/users", response_model=List[UserLocation])
def list_users():
    return DB
