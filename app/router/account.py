from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app import crud, model
from app.database import get_session

router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/")
def create(account_in: model.AccountIn, session: Session = Depends(get_session)):
    account_row = crud.account.get_by_name(session, account_in.name)
    if account_row is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    crud.account.create(session, account_in)


@router.get("/{id_}", response_model=model.AccountOut)
def read(id_: int, session: Session = Depends(get_session)):
    account_row = crud.account.get_full(session, id_)
    if account_row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")

    return account_row


@router.get("/", response_model=list[model.AccountOut])
def read_many(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    account_rows = crud.account.get_many_full(session, skip, limit)

    return account_rows


@router.put("/{id_}")
def update(id_: int, account_update: model.AccountUpdate, session: Session = Depends(get_session)):
    crud.account.update(session, id_, account_update)


@router.delete("/{id_}")
def delete(id_: int, session: Session = Depends(get_session)):
    crud.account.delete(session, id_)
