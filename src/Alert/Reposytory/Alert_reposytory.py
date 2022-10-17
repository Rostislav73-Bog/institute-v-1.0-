import asyncpg

import asyncio
# rabota s bd


async def alert():

    postgres_alert =  await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/postgres')

    await postgres_alert.execute('''
            create TABLE alert(
                id serial,
                name text,
                who text,
                cabinet numeric,
                problems text,
                status boolean
            )
        ''')
