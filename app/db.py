from datetime import datetime
from os import getenv
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine

load_dotenv()

db_user = getenv("POSTGRES_USER")
db_password = getenv("POSTGRES_PASSWORD")
db_host = getenv("POSTGRES_HOST")
db_name = getenv("POSTGRES_DB")

class Execution(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.now)
    commands: int
    result: int
    duration: float

DB_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_engine(DB_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]
