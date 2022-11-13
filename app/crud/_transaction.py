from app import model
from app.crud._base import CrudBase


class CrudTransaction(
    CrudBase[
        model.TransactionUpdate, model.TransactionIn, model.TransactionDb, model.TransactionOut
    ]
):
    pass


transaction = CrudTransaction(model.TransactionDb)
