from typing import TYPE_CHECKING, Optional

from sqlmodel import Relationship

from app.model._base import (
    ModelDatabaseBaseNamed,
    ModelInputBaseNamed,
    ModelOutputBaseNamed,
    ModelUpdateBaseNamed,
)

if TYPE_CHECKING:
    from app.model._transaction import TransactionDatabase


class CategoryInput(ModelInputBaseNamed):
    budget: float


class CategoryDatabase(ModelDatabaseBaseNamed, table=True):
    __tablename__ = "category"

    budget: float

    transactions: list["TransactionDatabase"] = Relationship(back_populates="category")


class CategoryOutput(ModelOutputBaseNamed):
    budget: float
    expenditure: float
    available: float


class CategoryUpdate(ModelUpdateBaseNamed):
    budget: Optional[float] = None
