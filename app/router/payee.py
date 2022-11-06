from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schema
from ..dependencies import get_db

router = APIRouter(
    prefix="/payee",
    tags=["payee"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create(payee: schema.PayeeIn, db: Session = Depends(get_db)):
    db_payee = crud.payee.get_by_name(db, payee.name)
    if db_payee is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    crud.payee.create(db, payee)


@router.get("/{id}", response_model=schema.PayeeOut)
def read(id: int, db: Session = Depends(get_db)):
    payee = crud.payee.get(db, id)
    if payee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Payee not found"
        )

    return payee


@router.get("/", response_model=list[schema.PayeeOut])
def read_all(db: Session = Depends(get_db)):
    payees = crud.payee.get_all(db)

    return payees


@router.put("/{id}")
def update(id: int, update: schema.PayeeUpdate, db: Session = Depends(get_db)):
    crud.payee.update(db, id, update)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    crud.payee.delete(db, id)
