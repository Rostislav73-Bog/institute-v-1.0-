from fastapi import FastAPI
from src.User.Controller import User_controller
from src.Alert.Controller import Alert_controller
from src.Alert.Reposytory import Alert_reposytory
from src.User.Reposytory import  User_reposytory
# from src.DataBase.DataBase import DataBaseModule
import asyncpg
import asyncio

# from src.Config import Config

app = FastAPI()
app.include_router(User_controller.user_router)
app.include_router(Alert_controller.alert_router)



@app.get("/")
async def main():  # connect front
    return "main"

# async def run():
#     app['DataBase'] = await asyncpg.create_pool(DataBaseModule)

@app.on_event("startup") #подключение к бд
async def startup():
     await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/postgres')


@app.post("/bla")  #создание бд
async def connect_postgres():
    await Alert_reposytory.alert()
    await User_reposytory.user()


@app.on_event("shutdown")
async def shutdown():
    asyncpg.connect('postgresql://postgres:postgres@localhost:5432/postgres').close()
