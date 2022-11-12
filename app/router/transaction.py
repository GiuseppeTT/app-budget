from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from .. import crud, model
from ..database import get_session

router = APIRouter(
    prefix="/transaction",
    tags=["transaction"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create(transaction_in: model.TransactionIn, session: Session = Depends(get_session)):
    crud.transaction.create(session, transaction_in)


@router.get("/{id}", response_model=model.TransactionOut)
def read(id: int, session: Session = Depends(get_session)):
    transaction_row = crud.transaction.get_full(session, id)
    if transaction_row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")

    return transaction_row


@router.get("/", response_model=list[model.TransactionOut])
def read_all(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    transaction_rows = crud.transaction.get_many_full(session, skip, limit)

    return transaction_rows


@router.put("/{id}")
def update(
    id: int, transaction_update: model.TransactionUpdate, session: Session = Depends(get_session)
):
    crud.transaction.update(session, id, transaction_update)


@router.delete("/{id}")
def delete(id: int, session: Session = Depends(get_session)):
    crud.transaction.delete(session, id)
