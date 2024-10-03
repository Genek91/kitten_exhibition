from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.crud import kitten_crud
from app.database import get_db
from app.api.validators import check_breed, check_kitten

kitten_router = APIRouter()


@kitten_router.get("/", response_model=list[schemas.Kitten])
def get_kittens(
    db: Session = Depends(get_db)
):
    return kitten_crud.get_kittens(db)


@kitten_router.get("/{kitten_id}", response_model=schemas.Kitten)
def get_kitten(
    kitten_id: int, db: Session = Depends(get_db)
):
    return check_kitten(kitten_id, db)


@kitten_router.get(
    "/breed/{breed}", response_model=list[schemas.Kitten]
)
def get_kittens_by_breed(
    breed: str, db: Session = Depends(get_db)
):
    return kitten_crud.get_kittens_by_breed(breed, db)


@kitten_router.post("/", response_model=schemas.Kitten)
def create_kitten(
    kitten: schemas.KittenCreate, db: Session = Depends(get_db)
):
    check_breed(kitten.breed_id, db)
    kitten_data = kitten.model_dump()
    return kitten_crud.create_kitten(kitten_data, db)


@kitten_router.put("/{kitten_id}", response_model=schemas.Kitten)
def update_kitten(
    kitten_id: int, kitten: schemas.KittenCreate, db: Session = Depends(get_db)
):
    check_breed(kitten.breed_id, db)
    kitten_db = check_kitten(kitten_id, db)
    kitten_data = kitten.model_dump()
    return kitten_crud.update_kitten(kitten_db, kitten_data, db)


@kitten_router.delete("/{kitten_id}")
def delete_kitten(
    kitten_id: int, db: Session = Depends(get_db)
):
    kitten_db = check_kitten(kitten_id, db)
    kitten_crud.delete_kitten(kitten_db, db)
