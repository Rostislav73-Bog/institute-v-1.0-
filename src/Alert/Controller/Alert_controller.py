from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel

alert_router = APIRouter()

class ModelSpeciality(str, Enum):
    null = "null"
    cleaning_women = "Уборщица"
    foremen = "Мастер участка"
    electrician = "Электромантер"
    plumber = "Сантехник"
    handyman = "Разнорабочий"

statuse = False

@alert_router.post("/creating_application")
async def creating(name: str, cabinet: int, who: ModelSpeciality, problems: str):
    return name, cabinet, who, problems, statuse
    # print()

@alert_router.get("/application_status")
async def status():
    return {"Статус заявки"}

@alert_router.patch("/applucation_processed")
async def applicarion_processing():
    return (statuse)