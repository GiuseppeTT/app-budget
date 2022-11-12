from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ._transaction import TransactionDb


class AccountUpdate(SQLModel):
    name: Optional[str] = None


class AccountBase(SQLModel):
    name: str = Field(unique=True, index=True)


class AccountIn(AccountBase):
    balance: float = 0


class AccountDb(AccountBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transactions: list["TransactionDb"] = Relationship(back_populates="account")


class AccountOut(AccountBase):
    id: int
    balance: float

    class Config:
        orm_mode = True
