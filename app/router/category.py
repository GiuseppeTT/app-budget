from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schema
from ..dependencies import get_db

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create(category: schema.CategoryIn, db: Session = Depends(get_db)):
    db_category = crud.category.get_by_name(db, category.name)
    if db_category is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name already registered"
        )

    crud.category.create(db, category)


@router.get("/{id}", response_model=schema.CategoryOut)
def read(id: int, db: Session = Depends(get_db)):
    category = crud.category.get(db, id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    # TODO: get_expenditure and get_available

    return category


@router.get("/", response_model=list[schema.CategoryOut])
def read_all(db: Session = Depends(get_db)):
    categories = crud.category.get_all(db)

    # TODO: get_expenditure and get_available

    return categories


@router.put("/{id}")
def update(id: int, update: schema.CategoryUpdate, db: Session = Depends(get_db)):
    crud.category.update(db, id, update)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    crud.category.delete(db, id)
