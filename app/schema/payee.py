from pydantic import BaseModel


class PayeeBase(BaseModel):
    name: str


class PayeeIn(PayeeBase):
    pass


class PayeeOut(PayeeBase):
    id: int

    class Config:
        orm_mode = True


class PayeeUpdate(PayeeBase):
    pass


class PayeeDatabase(PayeeBase):
    id: int
