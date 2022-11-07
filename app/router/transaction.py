from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schema
from ..dependencies import get_db

router = APIRouter(
    prefix="/transaction",
    tags=["transaction"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create(transaction: schema.TransactionIn, db: Session = Depends(get_db)):
    account = crud.account.get(db, transaction.account_id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )

    payee = crud.payee.get(db, transaction.payee_id)
    if payee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Payee not found"
        )

    category = crud.category.get(db, transaction.category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    crud.transaction.create(db, transaction)


@router.get("/{id}", response_model=schema.TransactionOut)
def read(id: int, db: Session = Depends(get_db)):
    transaction = crud.transaction.get(db, id)
    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found"
        )

    return transaction


@router.get("/", response_model=list[schema.TransactionOut])
def read_all(db: Session = Depends(get_db)):
    transactions = crud.transaction.get_all(db)

    return transactions


@router.put("/{id}")
def update(id: int, update: schema.TransactionUpdate, db: Session = Depends(get_db)):
    crud.transaction.update(db, id, update)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    crud.transaction.delete(db, id)
