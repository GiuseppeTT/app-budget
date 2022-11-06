from sqlalchemy.orm import Session

from .. import model, schema


def create(db: Session, transaction: schema.TransactionIn):
    transaction = model.Transaction(**transaction.dict())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)


def get(db: Session, id: int):
    return db.query(model.Transaction).filter(model.Transaction.id == id).first()


def get_all(db: Session):
    return db.query(model.Transaction).all()


def update(db: Session, id: int, update: schema.TransactionUpdate):
    transaction = get(db, id)

    if update.date_time is not None:
        transaction.date_time = update.date_time

    if update.account_id is not None:
        transaction.account_id = update.account_id

    if update.payee_id is not None:
        transaction.payee_id = update.payee_id

    if update.category_id is not None:
        transaction.category_id = update.category_id

    if update.value is not None:
        transaction.value = update.value

    if update.comment is not None:
        transaction.comment = update.comment

    db.add(transaction)
    db.commit()
    db.refresh(transaction)


def delete(db: Session, id: int):
    transaction = get(db, id)
    db.delete(transaction)
    db.commit()
