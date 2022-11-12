from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ._account import AccountDb
    from ._category import CategoryDb
    from ._payee import PayeeDb


class TransactionUpdate(SQLModel):
    date_time: Optional[datetime] = None
    account_id: Optional[int] = None
    payee_id: Optional[int] = None
    category_id: Optional[int] = None
    value: Optional[float] = None
    comment: Optional[str] = None


class TransactionBase(SQLModel):
    date_time: datetime = Field(default_factory=datetime.now)
    account_id: Optional[int] = Field(default=None, foreign_key="accountdb.id")
    payee_id: Optional[int] = Field(default=None, foreign_key="payeedb.id")
    category_id: Optional[int] = Field(default=None, foreign_key="categorydb.id")
    value: float
    comment: Optional[str] = None


class TransactionIn(TransactionBase):
    pass


class TransactionDb(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account: Optional["AccountDb"] = Relationship(back_populates="transactions")
    payee: Optional["PayeeDb"] = Relationship(back_populates="transactions")
    category: Optional["CategoryDb"] = Relationship(back_populates="transactions")


class TransactionOut(TransactionBase):
    id: int

    class Config:
        orm_mode = True
