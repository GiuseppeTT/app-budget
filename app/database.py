from sqlmodel import Session, SQLModel, create_engine

from app.config import settings

CONNECT_ARGS = {"check_same_thread": False}

engine = create_engine(settings.SQLITE_URL, connect_args=CONNECT_ARGS)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
