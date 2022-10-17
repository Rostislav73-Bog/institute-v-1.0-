import asyncpg
import asyncio
# class User_reposytory:
    # def create(create_user_data):
    #     #sql запрос на сощдания пользователя в таблицы Юсер из полей create_user_data
    #
    # def find(find_data):
    #     #sql
    #
    # def find_one(query_options):
    #     #ql

async def user():
    postgres_user = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/postgres')

    await postgres_user.execute('''
                create TABLE users(
                    id serial,
                    name text,
                    surname text,
                    password text,
                    phone numeric,
                    jwt text
                )
            ''')

