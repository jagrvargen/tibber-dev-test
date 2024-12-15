from datetime import datetime

import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from freezegun import freeze_time
from unittest.mock import patch

from ..main import app
from ..models.models import Executions

client = TestClient(app)

FIXED_TIME = "2024-12-14T21:20:23.132562"

@freeze_time(FIXED_TIME)
@patch("app.db.commit_execution")
def test_move_robot(mock_commit_execution):
    mock_execution = Executions(
            id=1,
            timestamp=datetime.now(),
            commands=1,
            result=2,
            duration=0.123,
    )

    resp = client.post(
            "/tibber-developer-test/enter-path/",
            json={"start": 
                  {"x": 0, "y": 0},
                  "commands": [
                      {"direction": "north", "steps": 1},
                  ]
            }
    )
    assert resp.status_code == 200
    assert resp.json() == jsonable_encoder(mock_execution)
