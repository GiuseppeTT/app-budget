from .. import model
from ._base import CrudBase


class CrudTransaction(
    CrudBase[
        model.TransactionUpdate, model.TransactionIn, model.TransactionDb, model.TransactionOut
    ]
):
    pass


transaction = CrudTransaction(model.TransactionDb)
