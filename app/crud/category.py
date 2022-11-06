from sqlalchemy.orm import Session

from .. import model, schema


def create(db: Session, category: schema.CategoryIn):
    category = model.Category(**category.dict())
    db.add(category)
    db.commit()
    db.refresh(category)


def get(db: Session, id: int):
    return db.query(model.Category).filter(model.Category.id == id).first()


def get_expenditure(db: Session, id: int):
    # TODO: Sum transaction values to get expenditure

    pass


def get_available(db: Session, id: int):
    # TODO: Sum transaction values to get expenditure
    # From budget and expenditure calculate available

    pass


def get_all(db: Session):
    return db.query(model.Category).all()


def update(db: Session, id: int, update: schema.CategoryUpdate):
    category = get(db, id)

    if update.name is not None:
        category.name = update.name

    if update.budget is not None:
        category.budget = update.budget

    db.add(category)
    db.commit()
    db.refresh(category)


def delete(db: Session, id: int):
    category = get(db, id)
    db.delete(category)
    db.commit()
