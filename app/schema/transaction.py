from datetime import datetime

from pydantic import BaseModel


class TransactionBase(BaseModel):
    id: int
    date_time: datetime
    account_id: int
    payee_id: int
    category_id: int
    value: float
    comment: str


class TransactionIn(TransactionBase):
    pass


class TransactionOut(TransactionBase):
    id: int

    class Config:
        orm_mode = True


class TransactionUpdate(TransactionBase):
    pass


class TransactionDatabase(TransactionBase):
    id: int
