from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_move_robot():
    resp = client.post(
            "/tibber-developer-test/enter-path/",
            json={"start": 
                  {
                      "x": 0, "y": 0
                    },
                  "commands": [
                      {
                        "direction": "north",
                        "steps": 1
                      }
                  ]
            }
    )
    assert resp.status_code == 200
    assert resp == {}
