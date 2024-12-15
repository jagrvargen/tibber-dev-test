import pytest
from fastapi.testcliet import TestClient
from testcontainer.postgres import PostgresContainer
from sqlmodel import create_engine, Session, SQLModel

from ..db import SessionDependency
from ..main import app

@pytest.fixture(scope="function")
def postgres_container():
    """Create a temporary Postgres container."""

    with PostgresContainer("postgres:15") as pg:
        test_engine = create_engine(postgres.get_connection_url())
        SQLModel.metadata.create_all(test_engine)
        
        with Session(test_engine) as session:
            yield session

@pytest.fixture
def client(postgres_container):
    """Mock the client and override the SessionDependency for testing."""

    app.dependency_overrides[SessionDependency] = lambda: postgres_container
    
    return TestClient(app)
