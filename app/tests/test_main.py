from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

from ..models.models import Executions, Command, Direction
from ..db import get_session, commit_execution
from .conftest import app, client

def test_move_robot_empty_commands(client):
    """Test robot movement with empty commands list"""
    test_payload = {
        "start": {"x": 0, "y": 0},
        "commands": []
    }
    response = client.post("/tibber-developer-test/enter-path/", json=test_payload)
    assert response.status_code == 200
    assert response.json() == {}

@patch('app.main.clean_office')
def test_move_robot_success(mock_clean_office, client):
    """Test successful robot movement with mocked database and cleaning function"""
    mock_clean_office.return_value = 5
    
    test_payload = {
        "start": {"x": 0, "y": 0},
        "commands": [
            {"direction": "north", "steps": 1},
            {"direction": "east", "steps": 2},
            {"direction": "south", "steps": 1},
        ]
    }

    response = client.post("/tibber-developer-test/enter-path/", json=test_payload)
    
    assert response.status_code == 200
    result = response.json()
    
    assert "id" in result
    assert "timestamp" in result
    assert result["commands"] == len(test_payload["commands"])
    assert result["result"] == 5
    assert "duration" in result
    
    expected_commands = [
        Command(direction=Direction(cmd["direction"]), steps=cmd["steps"])
        for cmd in test_payload["commands"]
    ]
    mock_clean_office.assert_called_once_with(0, 0, expected_commands)

def test_move_robot_invalid_input(client):
    """Test robot movement with invalid input"""
    test_payload = {
        "start": {"x": 0, "y": 0},
        "commands": [
            {"direction": "invalid", "steps": 1}
        ]
    }
    response = client.post("/tibber-developer-test/enter-path/", json=test_payload)
    assert response.status_code == 422

def test_commit_execution(client):
    """Test the commit_execution function"""
    execution = Executions(
        commands=3,
        result=5,
        duration=0.1
    )
    
    # Get session directly from the override function
    session = app.dependency_overrides[get_session]()
    
    result = commit_execution(execution, session)
    
    session.add.assert_called_once_with(execution)
    session.commit.assert_called_once()
    session.refresh.assert_called_once_with(execution)
    assert result == execution
