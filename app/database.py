from sqlmodel import Session, SQLModel, create_engine

from app.config import settings

database_url = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_FQDN}:5432/prod?sslmode=require"
engine = create_engine(database_url)


def create_database_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
