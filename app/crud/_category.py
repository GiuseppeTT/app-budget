from sqlmodel import Session, func, select

from app import model
from app.crud._base import CrudBaseNamed


class CrudCategory(
    CrudBaseNamed[model.CategoryUpdate, model.CategoryIn, model.CategoryDb, model.CategoryOut]
):
    def get_full(self, session: Session, id_: int):
        expenditure = func.ifnull(func.sum(model.TransactionDb.value), 0).label("expenditure")
        available = (self.model_db.budget + expenditure).label("available")
        statement = (
            select(
                self.model_db.id,
                self.model_db.name,
                self.model_db.budget,
                expenditure,
                available,
            )
            .join(model.TransactionDb, isouter=True)
            .where(self.model_db.id == id_)
        )
        result = session.exec(statement)
        row = result.first()

        return row

    def get_many_full(self, session: Session, skip: int, limit: int):
        expenditure = func.ifnull(func.sum(model.TransactionDb.value), 0).label("expenditure")
        available = (self.model_db.budget + expenditure).label("available")
        statement = (
            select(
                self.model_db.id,
                self.model_db.name,
                self.model_db.budget,
                expenditure,
                available,
            )
            .join(model.TransactionDb, isouter=True)
            .group_by(self.model_db.id)
            .offset(skip)
            .limit(limit)
        )
        result = session.exec(statement)
        rows = result.all()

        return rows


category = CrudCategory(model.CategoryDb)
