# Tibber Technical Case Development Test

### Summary
This is a toy microservice created as part of the interview process for a Backend Engineer position at Tibber. The project demonstrates the ability to build a simple microservice that processes movement commands and stores execution results in a PostgreSQL database.

### Prerequisites
- Docker
- Docker Compose
- Postman (optional, for testing)
- Python 3.11+
- pytest

### Setup Instructions

1. Clone the repository:
```bash
git clone git@github.com:jagrvargen/tibber-dev-test.git
cd tibber-dev-test
```

2. Create your environment file:
```bash
cp .env.example .env
```
You can modify the values in `.env` if needed, or use the default values provided.

3. Build and start the services:
```bash
docker-compose build
docker-compose up
```

### Running Tests

The project includes a test suite built with pytest. To run the tests:

1. Install the required Python packages (preferably in a virtual environment):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the test suite:
```bash
pytest tests/
```

For more verbose output, use:
```bash
pytest -v tests/
```

To generate a coverage report:
```bash
pytest --cov=src tests/
```

### Testing the Service

You can test the service using either Postman or curl by sending a POST request to:
```
http://localhost:5000/tibber-developer-test/enter-path
```

Example request body:
```json
{
  "start": {
    "x": 5,
    "y": 15
  },
  "commands": [
    {
      "direction": "south",
      "steps": 3
    },
    {
      "direction": "west",
      "steps": 4
    },
    {
      "direction": "north",
      "steps": 2
    }
  ]
}
```

Using curl:
```bash
curl -L -X POST \
  http://localhost:5000/tibber-developer-test/enter-path \
  -H 'Content-Type: application/json' \
  -d '{
    "start": {
      "x": 5,
      "y": 15
    },
    "commands": [
      {
        "direction": "south",
        "steps": 3
      },
      {
        "direction": "west",
        "steps": 4
      },
      {
        "direction": "north",
        "steps": 2
      }
    ]
  }'
```

### Checking the Database

To inspect the stored executions in the PostgreSQL database:

1. Access the PostgreSQL container:
```bash
docker exec -it tibber-dev-test-postgres-1 /bin/bash
```

2. Connect to the database:
```bash
psql -U [username] [database-name]
```

3. View the executions table:
```sql
SELECT * FROM executions;
```
