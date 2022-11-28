from sqlmodel import Session, SQLModel, create_engine

from app.config import settings

assert settings.PROD_DB_URL is not None

engine = create_engine(settings.PROD_DB_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
