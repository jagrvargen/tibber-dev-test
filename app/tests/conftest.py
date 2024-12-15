import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from app.main import app
from app.db.db import get_session, create_db_and_tables

@pytest.fixture(autouse=True)
def mock_db():
    """Mock database and engine operations"""
    with patch('app.db.db.engine'), \
         patch('app.db.db.create_db_and_tables'), \
         patch('app.main.create_db_and_tables'):
        yield

def create_mock_session():
    """Create a mock session for testing"""
    session = Mock()
    session.add = Mock()
    session.commit = Mock()
    session.refresh = Mock(side_effect=lambda x: setattr(x, 'id', 1))
    return session

@pytest.fixture
def client():
    """Test client fixture with mocked database session"""
    app.dependency_overrides[get_session] = create_mock_session
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()
