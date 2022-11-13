from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.model._transaction import TransactionDb


class PayeeIn(SQLModel):
    name: str


class PayeeDb(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    transactions: list["TransactionDb"] = Relationship(back_populates="payee")


class PayeeOut(SQLModel):
    id: int
    name: str
    expenditure: float

    class Config:
        orm_mode = True


class PayeeUpdate(SQLModel):
    name: Optional[str] = None
