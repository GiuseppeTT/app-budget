import abc
from typing import Generic, Optional, Type, TypeVar

from sqlmodel import Session, select

from app import model
from app.model import (
    ModelDatabaseBase,
    ModelDatabaseBaseNamed,
    ModelInputBase,
    ModelInputBaseNamed,
    ModelOutputBase,
    ModelOutputBaseNamed,
    ModelUpdateBase,
    ModelUpdateBaseNamed,
)

ModelInput = TypeVar("ModelInput", bound=ModelInputBase)
ModelDatabase = TypeVar("ModelDatabase", bound=ModelDatabaseBase)
ModelOutput = TypeVar("ModelOutput", bound=ModelOutputBase)
ModelUpdate = TypeVar("ModelUpdate", bound=ModelUpdateBase)

ModelInputNamed = TypeVar("ModelInputNamed", bound=ModelInputBaseNamed)
ModelDatabaseNamed = TypeVar("ModelDatabaseNamed", bound=ModelDatabaseBaseNamed)
ModelOutputNamed = TypeVar("ModelOutputNamed", bound=ModelOutputBaseNamed)
ModelUpdateNamed = TypeVar("ModelUpdateNamed", bound=ModelUpdateBaseNamed)


class CrudBase(Generic[ModelInput, ModelDatabase, ModelOutput, ModelUpdate], abc.ABC):
    def __init__(self, model_database: Type[ModelDatabase]):
        self.model_database = model_database

    def create(self, session: Session, input_: ModelInput) -> ModelDatabase:
        row = self.model_database(**input_.dict())
        session.add(row)
        session.commit()
        session.refresh(row)

        return row

    def get(self, session: Session, id_: int, none_ok: bool = True) -> Optional[ModelDatabase]:
        statement = select(self.model_database).where(self.model_database.id == id_)
        result = session.exec(statement)
        row = result.first()

        if none_ok:
            return row

        assert row is not None

        return row

    def get_many(self, session: Session, skip: int, limit: int) -> list[ModelDatabase]:
        statement = select(self.model_database).offset(skip).limit(limit)
        result = session.exec(statement)
        rows = result.all()

        return rows

    def update(self, session: Session, id_: int, update: ModelUpdate) -> ModelDatabase:
        row = self.get(session, id_)
        data_update = update.dict(exclude_unset=True)
        for key, value in data_update.items():
            setattr(row, key, value)
        session.add(row)
        session.commit()

        assert row is not None

        return row

    def delete(self, session: Session, id_: int) -> ModelDatabase:
        row = self.get(session, id_)
        session.delete(row)
        session.commit()

        assert row is not None

        return row

    def is_in_database(self, session: Session, id_: Optional[int], none_ok: bool = False) -> bool:
        if id_ is None:
            return none_ok

        row = self.get(session, id_, none_ok=True)
        in_database = row is not None

        return in_database


class CrudBaseNamed(
    CrudBase[ModelInputNamed, ModelDatabaseNamed, ModelOutputNamed, ModelUpdateNamed], abc.ABC
):
    def get_by_name(self, session: Session, name: str) -> Optional[ModelDatabaseNamed]:
        statement = select(self.model_database).where(self.model_database.name == name)
        result = session.exec(statement)
        row = result.first()

        return row

    @abc.abstractmethod
    def get_full(self, session: Session, id_: int):
        pass

    def _get_full(self, session: Session, id_: int, *args):
        statement = (
            select(self.model_database.id, self.model_database.name, *args)
            .join(model.TransactionDatabase, isouter=True)
            .where(self.model_database.id == id_)
        )
        result = session.exec(statement)
        row = result.first()

        return row

    @abc.abstractmethod
    def get_many_full(self, session: Session, skip: int, limit: int):
        pass

    def _get_many_full(self, session: Session, skip: int, limit: int, *args):
        statement = (
            select(self.model_database.id, self.model_database.name, *args)
            .join(model.TransactionDatabase, isouter=True)
            .group_by(self.model_database.id)
            .offset(skip)
            .limit(limit)
        )
        result = session.exec(statement)
        rows = result.all()

        return rows
