from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.model._account import AccountDb
    from app.model._category import CategoryDb
    from app.model._payee import PayeeDb


class TransactionIn(SQLModel):
    date_time: datetime = Field(default_factory=datetime.now)
    account_id: Optional[int] = None
    payee_id: Optional[int] = None
    category_id: Optional[int] = None
    value: float
    comment: Optional[str] = None


class TransactionDb(SQLModel, table=True):
    __tablename__ = "transaction"

    id: Optional[int] = Field(default=None, primary_key=True)
    date_time: datetime = Field(default_factory=datetime.now)
    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    payee_id: Optional[int] = Field(default=None, foreign_key="payee.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    value: float
    comment: Optional[str] = None

    account: Optional["AccountDb"] = Relationship(back_populates="transactions")
    payee: Optional["PayeeDb"] = Relationship(back_populates="transactions")
    category: Optional["CategoryDb"] = Relationship(back_populates="transactions")


class TransactionOut(SQLModel):
    id: int
    date_time: datetime
    account_id: Optional[int]
    payee_id: Optional[int]
    category_id: Optional[int]
    value: float
    comment: Optional[str]

    class Config:
        orm_mode = True


class TransactionUpdate(SQLModel):
    date_time: Optional[datetime] = None
    account_id: Optional[int] = None
    payee_id: Optional[int] = None
    category_id: Optional[int] = None
    value: Optional[float] = None
    comment: Optional[str] = None
