from fastapi import FastAPI

from .models.models import RobotMoveRequest 
from .move import clean_office

app = FastAPI()

@app.post("/tibber-developer-test/enter-path/")
async def move_robot(req: RobotMoveRequest):
    total_cleaned_tiles = clean_office(req.start.x, req.start.y, req.commands)
    return total_cleaned_tiles
