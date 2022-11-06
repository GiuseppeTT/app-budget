from pydantic import BaseModel


class AccountBase(BaseModel):
    name: str


class AccountIn(AccountBase):
    balance: float


class AccountOut(AccountBase):
    id: int
    balance: float

    class Config:
        orm_mode = True


class AccountUpdate(AccountBase):
    pass


class AccountDatabase(AccountBase):
    id: int
