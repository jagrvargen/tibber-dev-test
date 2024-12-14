from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from typing import Annotated, Literal

# Robot Movement Models
class Direction(str, Enum):
   north = "north"
   south = "south"
   east  = "east"
   west  = "west"

class Coords(BaseModel):
    x: int = Field(ge=-100000, le=100000)
    y: int = Field(ge=-100000, le=100000)

class Command(BaseModel):
    direction: Direction 
    steps: int = Field(gt=0, lt=100000)

class RobotMoveRequest(BaseModel):
    start: Coords
    commands: list[Command]

# DB Models
class Executions(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  timestamp: datetime = Field(default_factory=datetime.now)
  commands: int
  result: int
  duration: float
