from pydantic import BaseModel, Field
from typing import Annotated, Literal


class Coords(BaseModel):
    x: int = Field(ge=-100000, le=100000)
    y: int = Field(ge=-100000, le=100000)

class Command(BaseModel):
    direction: Literal["north", "south", "east", "west"]
    steps: int = Field(gt=0, lt=100000)

class RobotMoveRequest(BaseModel):
    start: Coords
    commands: list[Command]
