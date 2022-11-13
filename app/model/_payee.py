from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.model._transaction import TransactionDatabase


class PayeeInput(SQLModel):
    name: str


class PayeeDatabase(SQLModel, table=True):
    __tablename__ = "payee"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    transactions: list["TransactionDatabase"] = Relationship(back_populates="payee")


class PayeeOutput(SQLModel):
    id: int
    name: str
    expenditure: float

    class Config:
        orm_mode = True


class PayeeUpdate(SQLModel):
    name: Optional[str] = None
