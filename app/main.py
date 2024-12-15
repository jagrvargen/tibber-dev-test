from time import perf_counter

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from app.db import SessionDependency, create_db_and_tables, commit_execution
from app.models.models import Executions, RobotMoveRequest 
from app.actions.move import clean_office

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/tibber-developer-test/enter-path/")
async def move_robot(req: RobotMoveRequest, session: SessionDependency):
    if len(req.commands) == 0:
        return {}
    start_time = perf_counter()
    total_cleaned_tiles = clean_office(req.start.x, req.start.y, req.commands)
    end_time = perf_counter()

    execution = Executions(
            commands=len(req.commands),
            result=total_cleaned_tiles,
            duration=end_time-start_time,
    )
    
    refreshed_execution = commit_execution(execution, session)

    return jsonable_encoder(refreshed_execution)
