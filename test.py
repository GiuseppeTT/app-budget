from pathlib import Path

from sqlmodel import Session

from app import crud, model
from app.database import SQLITE_DB_PATH, create_db_and_tables, engine

Path(SQLITE_DB_PATH).unlink(missing_ok=True)

create_db_and_tables()

session = Session(engine)

################################################################################
# Create and read
crud.account.create(session, model.AccountInput(name="Savings"))
crud.account.create(session, model.AccountInput(name="Credit card"))
crud.account.create(session, model.AccountInput(name="Checking"))

print("\nAll accounts")
print(crud.account.get_many_full(session, skip=0, limit=100))

crud.payee.create(session, model.PayeeInput(name="Landlord"))
crud.payee.create(session, model.PayeeInput(name="Supermarket"))

print("\nAll payees")
print(crud.payee.get_many_full(session, skip=0, limit=100))

crud.category.create(session, model.CategoryInput(name="Rent", budget=1_000))
crud.category.create(session, model.CategoryInput(name="Food", budget=100))

print("\nAll categories")
print(crud.category.get_many_full(session, skip=0, limit=100))

crud.transaction.create(
    session,
    model.TransactionInput(
        account_id=1,
        payee_id=None,
        category_id=None,
        value=10_000,
        comment="Initial balance",
    ),
)

crud.transaction.create(
    session,
    model.TransactionInput(
        account_id=2,
        payee_id=None,
        category_id=None,
        value=1_000,
        comment="Initial balance",
    ),
)

crud.transaction.create(
    session,
    model.TransactionInput(
        account_id=3,
        payee_id=None,
        category_id=None,
        value=-100,
        comment="Initial balance",
    ),
)

crud.transaction.create(
    session,
    model.TransactionInput(
        account_id=1,
        payee_id=1,
        category_id=1,
        value=-1_000,
        comment="Rent (2022, May)",
    ),
)

crud.transaction.create(
    session,
    model.TransactionInput(
        account_id=2,
        payee_id=2,
        category_id=2,
        value=-12,
        comment="Ice cream and stuff",
    ),
)

crud.transaction.create(
    session,
    model.TransactionInput(
        account_id=2,
        payee_id=2,
        category_id=2,
        value=-13,
        comment="More ice cream and stuff",
    ),
)

print("\nAll transactions")
for transaction in crud.transaction.get_many(session, skip=0, limit=100):
    print(repr(transaction))

print("\nAll accounts")
print(crud.account.get_many_full(session, skip=0, limit=100))

print("\nAll categories")
print(crud.category.get_many_full(session, skip=0, limit=100))

################################################################################
# Update and read

crud.account.update(session, id_=1, update=model.AccountUpdate(name="Fake savings"))

print("\nAll accounts")
print(crud.account.get_many_full(session, skip=0, limit=100))

crud.payee.update(session, id_=1, update=model.PayeeUpdate(name="Fake landlord"))

print("\nAll payees")
print(crud.payee.get_many_full(session, skip=0, limit=100))

crud.category.update(session, id_=1, update=model.CategoryUpdate(name="Fake rent"))
crud.category.update(session, id_=2, update=model.CategoryUpdate(budget=90))

print("\nAll categories")
print(crud.category.get_many_full(session, skip=0, limit=100))

crud.transaction.update(
    session, id_=6, update=model.TransactionUpdate(comment="Fake more ice cream and stuff")
)

print("\nAll transactions")
for transaction in crud.transaction.get_many(session, skip=0, limit=100):
    print(repr(transaction))

################################################################################
# Delete and read

crud.account.delete(session, id_=1)

print("\nAll accounts")
print(crud.account.get_many_full(session, skip=0, limit=100))

print("\nAll transactions")
for transaction in crud.transaction.get_many(session, skip=0, limit=100):
    print(repr(transaction))


crud.payee.delete(session, id_=1)

print("\nAll payees")
print(crud.payee.get_many_full(session, skip=0, limit=100))

print("\nAll transactions")
for transaction in crud.transaction.get_many(session, skip=0, limit=100):
    print(repr(transaction))

crud.category.delete(session, id_=1)

print("\nAll categories")
print(crud.category.get_many_full(session, skip=0, limit=100))

print("\nAll transactions")
for transaction in crud.transaction.get_many(session, skip=0, limit=100):
    print(repr(transaction))
