from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from ._transaction import TransactionDb


class CategoryUpdate(SQLModel):
    name: Optional[str] = None
    budget: Optional[float] = None


class CategoryBase(SQLModel):
    name: str = Field(unique=True, index=True)
    budget: float


class CategoryIn(CategoryBase):
    pass


class CategoryDb(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transactions: list["TransactionDb"] = Relationship(back_populates="category")


class CategoryOut(CategoryBase):
    id: int
    expenditure: float
    available: float

    class Config:
        orm_mode = True
