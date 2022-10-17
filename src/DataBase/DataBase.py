# поделючение к бд и все что связано с бд
import asyncpg
import asyncio

from src.main import app




class DataBaseModule:

    @app.on_event("startup")
    async def startup(self):
        await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/postgres')

    @app.on_event("shutdown")
    async def shutdown(self):
        await asyncpg.disconnect('postgresql://postgres:postgres@localhost:5432/postgres')
#

