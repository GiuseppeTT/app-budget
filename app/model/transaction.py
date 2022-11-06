from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from ..database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    payee_id = Column(Integer, ForeignKey("payees.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    value = Column(Float)
    comment = Column(String)
