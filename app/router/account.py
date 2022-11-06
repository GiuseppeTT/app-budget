from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schema
from ..dependencies import get_db

router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create(account: schema.AccountIn, db: Session = Depends(get_db)):
    db_account = crud.account.get_by_name(db, account.name)
    if db_account is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    crud.account.create(db, account)

    # TODO: create_initial_transaction


@router.get("/{id}", response_model=schema.AccountOut)
def read(id: int, db: Session = Depends(get_db)):
    account = crud.account.get(db, id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )

    # TODO: get_balance

    return account


@router.get("/", response_model=list[schema.AccountOut])
def read_all(db: Session = Depends(get_db)):
    accounts = crud.account.get_all(db)

    # TODO: get_balance

    return accounts


@router.put("/{id}")
def update(id: int, update: schema.AccountUpdate, db: Session = Depends(get_db)):
    crud.account.update(db, id, update)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    crud.account.delete(db, id)
