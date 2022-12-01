import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.config import settings
from app.dependency import get_session
from app.main import app


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(settings.TEST_DATABASE_URL, poolclass=StaticPool)

    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)

    yield client

    app.dependency_overrides.clear()
