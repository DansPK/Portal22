import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine


@pytest.fixture(scope="session", autouse=True)
def create_tables():
    Base.metadata.create_all(bind=engine)


@pytest.fixture()
def client():
    return TestClient(app)
