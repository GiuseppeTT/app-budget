from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship

from app.model._base import ModelDatabaseBase, ModelInputBase, ModelOutputBase, ModelUpdateBase

if TYPE_CHECKING:
    from app.model._account import AccountDatabase
    from app.model._category import CategoryDatabase
    from app.model._payee import PayeeDatabase


class TransactionInput(ModelInputBase):
    date_time: datetime = Field(default_factory=datetime.now)
    account_id: Optional[int] = None
    payee_id: Optional[int] = None
    category_id: Optional[int] = None
    value: float
    comment: Optional[str] = None


class TransactionDatabase(ModelDatabaseBase, table=True):
    __tablename__ = "transaction"

    date_time: datetime = Field(default_factory=datetime.now)
    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    payee_id: Optional[int] = Field(default=None, foreign_key="payee.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    value: float
    comment: Optional[str] = None

    account: Optional["AccountDatabase"] = Relationship(back_populates="transactions")
    payee: Optional["PayeeDatabase"] = Relationship(back_populates="transactions")
    category: Optional["CategoryDatabase"] = Relationship(back_populates="transactions")


class TransactionOutput(ModelOutputBase):
    date_time: datetime
    account_id: Optional[int]
    payee_id: Optional[int]
    category_id: Optional[int]
    value: float
    comment: Optional[str]


class TransactionUpdate(ModelUpdateBase):
    date_time: Optional[datetime] = None
    account_id: Optional[int] = None
    payee_id: Optional[int] = None
    category_id: Optional[int] = None
    value: Optional[float] = None
    comment: Optional[str] = None
