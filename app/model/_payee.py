from typing import TYPE_CHECKING

from sqlmodel import Relationship

from app.model._base import (
    ModelDatabaseBaseNamed,
    ModelInputBaseNamed,
    ModelOutputBaseNamed,
    ModelUpdateBaseNamed,
)

if TYPE_CHECKING:
    from app.model._transaction import TransactionDatabase


class PayeeInput(ModelInputBaseNamed):
    pass


class PayeeDatabase(ModelDatabaseBaseNamed, table=True):
    __tablename__ = "payee"

    transactions: list["TransactionDatabase"] = Relationship(back_populates="payee")


class PayeeOutput(ModelOutputBaseNamed):
    expenditure: float


class PayeeUpdate(ModelUpdateBaseNamed):
    pass
