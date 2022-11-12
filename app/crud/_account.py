from sqlmodel import Session, func, select

from .. import model
from ._base import CrudBaseNamed


class CrudAccount(
    CrudBaseNamed[model.AccountUpdate, model.AccountIn, model.AccountDb, model.AccountOut]
):
    def create(self, session: Session, object_in: model.AccountIn) -> None:
        row = self.model_db(**object_in.dict())
        row_transaction = model.TransactionDb(
            account=row,
            value=object_in.balance,
            comment="Initial balance",
        )
        session.add(row)
        session.add(row_transaction)
        session.commit()

    def get_full(self, session: Session, id: int):
        balance = func.sum(model.TransactionDb.value).label("balance")
        statement = (
            select(self.model_db.id, self.model_db.name, balance)
            .join(model.TransactionDb, isouter=True)
            .where(self.model_db.id == id)
        )
        result = session.exec(statement)
        row = result.first()

        return row

    def get_many_full(self, session: Session, skip: int, limit: int):
        balance = func.sum(model.TransactionDb.value).label("balance")
        statement = (
            select(self.model_db.id, self.model_db.name, balance)
            .join(model.TransactionDb, isouter=True)
            .group_by(self.model_db.id)
            .offset(skip)
            .limit(limit)
        )
        result = session.exec(statement)
        rows = result.all()

        return rows


account = CrudAccount(model.AccountDb)
