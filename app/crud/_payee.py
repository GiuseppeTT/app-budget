from .. import model
from ._base import CrudBaseNamed


class CrudPayee(CrudBaseNamed[model.PayeeUpdate, model.PayeeIn, model.PayeeDb, model.PayeeOut]):
    pass


payee = CrudPayee(model.PayeeDb)
