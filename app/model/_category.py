from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ._transaction import TransactionDb


class CategoryIn(SQLModel):
    name: str
    budget: float


class CategoryDb(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    budget: float

    transactions: list["TransactionDb"] = Relationship(back_populates="category")


class CategoryOut(SQLModel):
    id: int
    name: str
    budget: float
    expenditure: float
    available: float

    class Config:
        orm_mode = True


class CategoryUpdate(SQLModel):
    name: Optional[str] = None
    budget: Optional[float] = None
