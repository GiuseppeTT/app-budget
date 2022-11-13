from sqlmodel import Session, func, select

from .. import model
from ._base import CrudBaseNamed


class CrudPayee(CrudBaseNamed[model.PayeeUpdate, model.PayeeIn, model.PayeeDb, model.PayeeOut]):
    def get_full(self, session: Session, id: int):
        expenditure = func.ifnull(func.sum(model.TransactionDb.value), 0).label("expenditure")
        statement = (
            select(self.model_db.id, self.model_db.name, expenditure)
            .join(model.TransactionDb, isouter=True)
            .where(self.model_db.id == id)
        )
        result = session.exec(statement)
        row = result.first()

        return row

    def get_many_full(self, session: Session, skip: int, limit: int):
        expenditure = func.ifnull(func.sum(model.TransactionDb.value), 0).label("expenditure")
        statement = (
            select(self.model_db.id, self.model_db.name, expenditure)
            .join(model.TransactionDb, isouter=True)
            .group_by(self.model_db.id)
            .offset(skip)
            .limit(limit)
        )
        result = session.exec(statement)
        rows = result.all()

        return rows


payee = CrudPayee(model.PayeeDb)
