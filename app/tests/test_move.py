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


def test_ten_thousand_commands():
    """Test robot movement with 10,000 commands"""
    commands = [
        Command(direction=Direction.north, steps=1),
    ] * 10000

    result = clean_office(0, 0, commands)

    assert result == 10001


def test_move_robot_large_scale_pattern():
    """Test that the move command works with large inputs"""
    base_commands = [
        Command(direction=Direction.east, steps=99999),
        Command(direction=Direction.north, steps=99999),
        Command(direction=Direction.west, steps=99998),
        Command(direction=Direction.south, steps=99998),
    ]

    commands = []
    for _ in range(2500):
        commands.extend(base_commands)

    result = clean_office(-100000, -100000, commands)
    expected_coverage = 993737501

    assert result == expected_coverage
