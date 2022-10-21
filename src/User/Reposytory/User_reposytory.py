# class User_reposytory:
    # def create(create_user_data):
    #     #sql запрос на сощдания пользователя в таблицы Юсер из полей create_user_data
    #
    # def find(find_data):
    #     #sql
    #
    # def find_one(query_options):
    #     #ql
from pydantic import BaseModel
import sqlalchemy
import databases
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("surname", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.Text),
    sqlalchemy.Column("phone", sqlalchemy.Numeric),
    sqlalchemy.Column("jwt", sqlalchemy.Text),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

class Users_registration(BaseModel):
    name: str
    surname: str
    password: str
    phone: int
    jwt: str
