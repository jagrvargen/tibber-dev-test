import pytest

from app.actions.move import clean_office
from app.models.models import Direction, Command

def test_move_robot_success():
    """Test successful robot movement"""
    commands = [
        Command(direction=Direction.north, steps=1),
        Command(direction=Direction.east, steps=2),
        Command(direction=Direction.south, steps=1),
    ]

    result = clean_office(0, 0, commands)

    assert result == 5

def test_move_robot_success_same_tile_counted_once():
    """Test that going over the same tile isn't counted more than once"""
    commands = [
        Command(direction=Direction.north, steps=1),
        Command(direction=Direction.south, steps=1),
        Command(direction=Direction.north, steps=1),
        Command(direction=Direction.south, steps=1),
    ]

    result = clean_office(0, 0, commands)

    assert result == 2

def test_move_robot_alternate_starting_position():
    """Test robot movement with a different starting position"""
    commands = [
        Command(direction=Direction.north, steps=1),
        Command(direction=Direction.east, steps=2),
        Command(direction=Direction.south, steps=1),
    ]

    result = clean_office(1, 1, commands)

    assert result == 5
