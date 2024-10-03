from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.crud import breed_crud
from app.database import get_db
from app.api.validators import check_unique_breed

breed_router = APIRouter()


@breed_router.get("/", response_model=list[schemas.Breed])
def get_breeds(
    db: Session = Depends(get_db)
):
    return breed_crud.get_breeds(db)


@breed_router.post("/", response_model=schemas.Breed)
def create_breed(
    breed: schemas.BreedCreate, db: Session = Depends(get_db)
):
    check_unique_breed(breed.name, db)
    breed_data = breed.model_dump()
    return breed_crud.create_breed(breed_data, db)
