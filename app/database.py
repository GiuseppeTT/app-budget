from sqlmodel import Session, SQLModel, create_engine

from app.config import settings

assert settings.PROD_DATABASE_URL is not None

engine = create_engine(settings.PROD_DATABASE_URL)


def create_database_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
