from sqlalchemy.orm import Session

from .. import model, schema


def create(db: Session, account: schema.AccountIn):
    account = model.Account(name=account.name)
    db.add(account)
    db.commit()
    db.refresh(account)


def create_initial_transaction(db: Session, account: schema.AccountIn):
    # TODO: Set transaction for initial account balance

    pass


def get(db: Session, id: int):
    return db.query(model.Account).filter(model.Account.id == id).first()


def get_by_name(db: Session, name: str):
    return db.query(model.Account).filter(model.Account.name == name).first()


def get_balance(db: Session, id: int):
    # TODO: Sum transaction values to get balance

    pass


def get_all(db: Session):
    return db.query(model.Account).all()


def update(db: Session, id: int, update: schema.AccountUpdate):
    account = get(db, id)
    account.name = update.name

    db.add(account)
    db.commit()
    db.refresh(account)


def delete(db: Session, id: int):
    account = get(db, id)
    db.delete(account)
    db.commit()
