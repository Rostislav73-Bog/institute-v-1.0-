# rabota s bd

import sqlalchemy
import databases
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

alert = sqlalchemy.Table(
    "alert",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("who", sqlalchemy.String),
    sqlalchemy.Column("cabinet", sqlalchemy.Integer),
    sqlalchemy.Column("problems", sqlalchemy.Text),
    sqlalchemy.Column("status", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("date", sqlalchemy.DateTime),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)