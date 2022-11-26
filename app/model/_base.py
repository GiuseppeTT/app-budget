from typing import Optional

from sqlmodel import Field, SQLModel


class ModelInputBase(SQLModel):
    pass


class ModelDatabaseBase(SQLModel):
    id: int = Field(default=None, primary_key=True)  # Can be None when not committed, but don't tell mypy 🤫


class ModelOutputBase(SQLModel):
    id: int

    class Config:
        orm_mode = True


class ModelUpdateBase(SQLModel):
    pass


class ModelInputBaseNamed(ModelInputBase):
    name: str


class ModelDatabaseBaseNamed(ModelDatabaseBase):
    name: str = Field(unique=True, index=True)


class ModelOutputBaseNamed(ModelOutputBase):
    name: str


class ModelUpdateBaseNamed(ModelUpdateBase):
    name: Optional[str] = None
