from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.model._transaction import TransactionDatabase


class CategoryInput(SQLModel):
    name: str
    budget: float


class CategoryDatabase(SQLModel, table=True):
    __tablename__ = "category"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    budget: float

    transactions: list["TransactionDatabase"] = Relationship(back_populates="category")


class CategoryOutput(SQLModel):
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
