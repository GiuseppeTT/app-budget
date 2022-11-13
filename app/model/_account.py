from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ._transaction import TransactionDb


class AccountIn(SQLModel):
    name: str


class AccountDb(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    transactions: list["TransactionDb"] = Relationship(back_populates="account")


class AccountOut(SQLModel):
    id: int
    name: str
    balance: float

    class Config:
        orm_mode = True


class AccountUpdate(SQLModel):
    name: Optional[str] = None
