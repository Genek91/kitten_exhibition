from sqlalchemy.orm import Session
from sqlalchemy.future import select

from app import models
from app.crud.base import get_object, get_objects, create_object


def get_breeds(db: Session):
    return get_objects(models.Breed, db)


def get_breed(breed_id: int, db: Session):
    return get_object(models.Breed, breed_id, db)


def get_breed_by_name(breed: str, db: Session):
    return db.execute(
        select(models.Breed).where(models.Breed.name == breed)
    ).scalar_one_or_none()


def create_breed(breed_data: dict, db: Session):
    db_breed = models.Breed(**breed_data)
    return create_object(db_breed, db)
