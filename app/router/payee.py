from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from .. import crud, model
from ..database import get_session

router = APIRouter(
    prefix="/payee",
    tags=["payee"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create(payee_in: model.PayeeIn, session: Session = Depends(get_session)):
    payee_row = crud.payee.get_by_name(session, payee_in.name)
    if payee_row is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    crud.payee.create(session, payee_in)


@router.get("/{id_}", response_model=model.PayeeOut)
def read(id_: int, session: Session = Depends(get_session)):
    payee_row = crud.payee.get_full(session, id_)
    if payee_row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payee not found")

    return payee_row


@router.get("/", response_model=list[model.PayeeOut])
def read_many(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    payees = crud.payee.get_many_full(session, skip, limit)

    return payees


@router.put("/{id_}")
def update(id_: int, payee_update: model.PayeeUpdate, session: Session = Depends(get_session)):
    crud.payee.update(session, id_, payee_update)


@router.delete("/{id_}")
def delete(id_: int, session: Session = Depends(get_session)):
    crud.payee.delete(session, id_)
