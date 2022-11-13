from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app import crud, model
from app.database import get_session

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/")
def create(category_in: model.CategoryIn, session: Session = Depends(get_session)):
    category_row = crud.category.get_by_name(session, category_in.name)
    if category_row is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    crud.category.create(session, category_in)


@router.get("/{id_}", response_model=model.CategoryOut)
def read(id_: int, session: Session = Depends(get_session)):
    category_row = crud.category.get_full(session, id_)
    if category_row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return category_row


@router.get("/", response_model=list[model.CategoryOut])
def read_many(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    categorie_rows = crud.category.get_many_full(session, skip, limit)

    return categorie_rows


@router.put("/{id_}")
def update(
    id_: int, category_update: model.CategoryUpdate, session: Session = Depends(get_session)
):
    crud.category.update(session, id_, category_update)


@router.delete("/{id_}")
def delete(id_: int, session: Session = Depends(get_session)):
    crud.category.delete(session, id_)
