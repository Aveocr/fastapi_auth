from pydantic import Field, BaseModel
from sqlalchemy import Column, Boolean, Integer, String, MetaData, Table, ForeignKey, JSON

metadata = MetaData()


users = Table(
    "USER",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("hash_password", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("sex", Boolean, nullable=False),
    Column("email", String, nullable=False)

)

tasks = Table(
    "TASK",
    metadata,
    Column("task_id", Integer, primary_key=True),
    Column("text", String, nullable=True),
    Column("user_id", Integer, ForeignKey("users.user_id"))

)
#