from sqlmodel import Session, func

from app import model
from app.crud._base import CrudBaseNamed


class CrudAccount(
    CrudBaseNamed[
        model.AccountInput, model.AccountDatabase, model.AccountOutput, model.AccountUpdate
    ]
):
    def get_full(self, session: Session, id_: int):
        balance = func.ifnull(func.sum(model.TransactionDatabase.value), 0).label("balance")
        row = self._get_full(session, id_, balance)

        return row

    def get_many_full(self, session: Session, skip: int, limit: int):
        balance = func.ifnull(func.sum(model.TransactionDatabase.value), 0).label("balance")
        rows = self._get_many_full(session, skip, limit, balance)

        return rows


account = CrudAccount(model.AccountDatabase)
