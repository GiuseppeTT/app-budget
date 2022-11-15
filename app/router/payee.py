from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app import crud, model
from app.database import get_session

router = APIRouter(
    prefix="/payee",
    tags=["payee"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/", response_model=model.PayeeOutput)
def create(input_: model.PayeeInput, session: Session = Depends(get_session)):
    found_row = crud.payee.get_by_name(session, input_.name)
    if found_row is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    row = crud.payee.create(session, input_)
    full_row = crud.payee.get_full(session, row.id)

    return full_row


@router.get("/{id_}", response_model=model.PayeeOutput)
def read(id_: int, session: Session = Depends(get_session)):
    full_row = crud.payee.get_full(session, id_)
    if full_row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payee not found")

    return full_row


@router.get("/", response_model=list[model.PayeeOutput])
def read_many(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    full_rows = crud.payee.get_many_full(session, skip, limit)

    return full_rows


@router.put("/{id_}", response_model=model.PayeeOutput)
def update(id_: int, update_: model.PayeeUpdate, session: Session = Depends(get_session)):
    row = crud.payee.update(session, id_, update_)
    full_row = crud.payee.get_full(session, row.id)

    return full_row


@router.delete("/{id_}", response_model=model.PayeeOutput)
def delete(id_: int, session: Session = Depends(get_session)):
    full_row = crud.payee.get_full(session, id_)
    crud.payee.delete(session, id_)

    return full_row
