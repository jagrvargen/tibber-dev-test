from datetime import datetime
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine

from .main import app

load_dotenv()

class Execution(SQLModel, table=True):
    id: int = Field(primary_key=True)
    timestamp: datetime
    commands: int
    result: int
    duration: float

DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

engine = create_engine(DB_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
