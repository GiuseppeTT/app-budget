from fastapi import FastAPI

from .database import create_db_and_tables
from .router import account, category, payee, transaction

create_db_and_tables()

app = FastAPI()


app.include_router(account.router)
app.include_router(payee.router)
app.include_router(category.router)
app.include_router(transaction.router)
