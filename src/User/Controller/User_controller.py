from fastapi import APIRouter
from typing import List
from src.User.Reposytory.User_reposytory import Users_registration, users
from src.User.Reposytory.User_reposytory import database
# from src.main import startup
user_router = APIRouter()

@user_router.on_event("startup")
async def startup():
    await database.connect()
    print("connect in routers")
@user_router.post("/registration", response_model=Users_registration)
async def registration(user:Users_registration):
    query = users.insert().values(name=user.name, surname=user.surname, password=user.password, phone=user.phone)
    meaning = await database.execute(query)
    return {**user.dict()}

@user_router.post("/authorization")
async def authorization(name: str, password: str):
    return name, password
