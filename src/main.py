from fastapi import FastAPI
from src.User.Controller import User_controller
from src.Alert.Controller import Alert_controller
from src.Alert.Reposytory import Alert_reposytory
from src.User.Reposytory import  User_reposytory
from src.Alert.Reposytory.Alert_reposytory import database
# from src.Config import Config

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    print("connect")


@app.get("/")
async def main():  # connect front
    query_user = User_reposytory.users.select()
    await database.fetch_all(query_user)
    query_alert = Alert_reposytory.alert.select()
    await database.fetch_all(query_alert)
    return "main"

app.include_router(User_controller.user_router)
app.include_router(Alert_controller.alert_router)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print("disconnect")
