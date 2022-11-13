from app import model
from app.crud._base import CrudBase


class CrudTransaction(
    CrudBase[
        model.TransactionInput,
        model.TransactionDatabase,
        model.TransactionOutput,
        model.TransactionUpdate,
    ]
):
    pass


transaction = CrudTransaction(model.TransactionDatabase)
