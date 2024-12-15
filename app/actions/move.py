from enum import Enum

from app.models.models import Command, Direction

def clean_office(x: int, y: int, commands: list[Command]):
    cleaned_tiles = set()
    cleaned_tiles.add((x, y))
    directions = {
            Direction.north: (-1, 0),
            Direction.south: (1, 0),
            Direction.east: (0, 1),
            Direction.west: (0, -1),
    }
    for command in commands:
        dx, dy = directions[command.direction]
        steps = command.steps
        for _ in range(steps):
            x += dx
            y += dy
            cleaned_tiles.add((x, y))
    
    return len(cleaned_tiles)
