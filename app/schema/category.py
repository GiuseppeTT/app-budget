from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    budget: float


class CategoryIn(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int
    expenditure: float
    available: float

    class Config:
        orm_mode = True


class CategoryUpdate(CategoryBase):
    pass


class CategoryDatabase(CategoryBase):
    id: int
