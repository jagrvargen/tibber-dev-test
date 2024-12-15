from datetime import datetime
from os import getenv
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from app.models.models import Executions

load_dotenv()

db_user = getenv("POSTGRES_USER")
db_password = getenv("POSTGRES_PASSWORD")
db_host = getenv("POSTGRES_HOST")
db_name = getenv("POSTGRES_DB")

DB_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_engine(DB_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]

def commit_execution(execution: Executions, session: SessionDependency):
    session.add(execution)
    session.commit()
    session.refresh(execution)

    return execution
