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


class AccountInput(ModelInputBaseNamed):
    pass


class AccountDatabase(ModelDatabaseBaseNamed, table=True):
    __tablename__ = "account"

    transactions: list["TransactionDatabase"] = Relationship(back_populates="account")


class AccountOutput(ModelOutputBaseNamed):
    balance: float


class AccountUpdate(ModelUpdateBaseNamed):
    pass
