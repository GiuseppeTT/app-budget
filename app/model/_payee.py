from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ._transaction import TransactionDb


class PayeeUpdate(SQLModel):
    name: Optional[str] = None


class PayeeBase(SQLModel):
    name: str = Field(unique=True, index=True)


class PayeeIn(PayeeBase):
    pass


class PayeeDb(PayeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transactions: list["TransactionDb"] = Relationship(back_populates="payee")


class PayeeOut(PayeeBase):
    id: int

    class Config:
        orm_mode = True
