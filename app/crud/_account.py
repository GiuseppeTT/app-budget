from sqlmodel import Session, func, select

from .. import model
from ._base import CrudBaseNamed


class CrudAccount(
    CrudBaseNamed[model.AccountUpdate, model.AccountIn, model.AccountDb, model.AccountOut]
):
    def get_full(self, session: Session, id_: int):
        balance = func.ifnull(func.sum(model.TransactionDb.value), 0).label("balance")
        statement = (
            select(self.model_db.id, self.model_db.name, balance)
            .join(model.TransactionDb, isouter=True)
            .where(self.model_db.id == id_)
        )
        result = session.exec(statement)
        row = result.first()

        return row

    def get_many_full(self, session: Session, skip: int, limit: int):
        balance = func.ifnull(func.sum(model.TransactionDb.value), 0).label("balance")
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
