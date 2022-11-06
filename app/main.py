from fastapi import FastAPI

from .database import Base, engine
from .router import account, category, payee, transaction

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(account.router)
app.include_router(payee.router)
app.include_router(category.router)
app.include_router(transaction.router)
