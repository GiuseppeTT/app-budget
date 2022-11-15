from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app import crud, model
from app.database import get_session

router = APIRouter(
    prefix="/transaction",
    tags=["transaction"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/", response_model=model.TransactionOutput)
def create(input_: model.TransactionInput, session: Session = Depends(get_session)):
    row = crud.transaction.create(session, input_)

    return row


@router.get("/{id_}", response_model=model.TransactionOutput)
def read(id_: int, session: Session = Depends(get_session)):
    row = crud.transaction.get(session, id_)
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")

    return row


@router.get("/", response_model=list[model.TransactionOutput])
def read_many(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    rows = crud.transaction.get_many(session, skip, limit)

    return rows


@router.put("/{id_}", response_model=model.TransactionOutput)
def update(id_: int, update_: model.TransactionUpdate, session: Session = Depends(get_session)):
    row = crud.transaction.update(session, id_, update_)

    return row


@router.delete("/{id_}", response_model=model.TransactionOutput)
def delete(id_: int, session: Session = Depends(get_session)):
    row = crud.transaction.delete(session, id_)

    return row
