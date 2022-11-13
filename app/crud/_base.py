from typing import Generic, Optional, Type, TypeVar

from sqlmodel import Session, SQLModel, select

ModelUpdate = TypeVar("ModelUpdate", bound=SQLModel)
ModelIn = TypeVar("ModelIn", bound=SQLModel)
ModelDb = TypeVar("ModelDb", bound=SQLModel)
ModelOut = TypeVar("ModelOut", bound=SQLModel)


class CrudBase(Generic[ModelUpdate, ModelIn, ModelDb, ModelOut]):
    def __init__(self, model_db: Type[ModelDb]):
        self.model_db = model_db

    def create(self, session: Session, object_in: ModelIn) -> None:
        row = self.model_db(**object_in.dict())
        session.add(row)
        session.commit()

    def get(self, session: Session, id_: int) -> Optional[ModelDb]:
        statement = select(self.model_db).where(self.model_db.id == id_)
        result = session.exec(statement)
        row = result.first()

        return row

    def get_full(self, session: Session, id_: int):
        return self.get(session, id_)

    def get_many(self, session: Session, skip: int, limit: int) -> list[ModelDb]:
        statement = select(self.model_db).offset(skip).limit(limit)
        result = session.exec(statement)
        rows = result.all()

        return rows

    def get_many_full(self, session: Session, skip: int, limit: int):
        return self.get_many(session, skip, limit)

    def update(self, session: Session, id_: int, object_update: ModelUpdate) -> None:
        row = self.get(session, id_)
        data_update = object_update.dict(exclude_unset=True)
        for key, value in data_update.items():
            setattr(row, key, value)
        session.add(row)
        session.commit()

    def delete(self, session: Session, id_: int) -> None:
        row = self.get(session, id_)
        session.delete(row)
        session.commit()


class CrudBaseNamed(CrudBase[ModelUpdate, ModelIn, ModelDb, ModelOut]):
    def get_by_name(self, session: Session, name: str) -> Optional[ModelDb]:
        statement = select(self.model_db).where(self.model_db.name == name)
        result = session.exec(statement)
        row = result.first()

        return row
