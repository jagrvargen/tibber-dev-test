from fastapi import FastAPI

from .models.models import RobotMoveRequest 

app = FastAPI()

@app.post("/tibber-developer-test/enter-path/")
async def move_robot(req: RobotMoveRequest):
    return req
