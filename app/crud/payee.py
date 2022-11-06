from sqlalchemy.orm import Session

from .. import model, schema


def create(db: Session, payee: schema.PayeeIn):
    payee = model.Payee(**payee.dict())
    db.add(payee)
    db.commit()
    db.refresh(payee)


def get(db: Session, id: int):
    return db.query(model.Payee).filter(model.Payee.id == id).first()


def get_by_name(db: Session, name: str):
    return db.query(model.Payee).filter(model.Payee.name == name).first()


def get_all(db: Session):
    return db.query(model.Payee).all()


def update(db: Session, id: int, update: schema.PayeeUpdate):
    payee = get(db, id)
    payee.name = update.name

    db.add(payee)
    db.commit()
    db.refresh(payee)


def delete(db: Session, id: int):
    payee = get(db, id)
    db.delete(payee)
    db.commit()
