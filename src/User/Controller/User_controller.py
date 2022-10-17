from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/registration")
async def registration(name: str, surname: str, password: str, number: int):
    return name, surname, password, number


@user_router.post("/authorization")
async def authorization(name: str, password: str):
    return name, password
