from sqlalchemy.orm import Session
from sqlalchemy.future import select

from app import models
from app.crud.base import (get_object, get_objects, create_object,
                           update_object, delete_object)


def get_kittens(db: Session):
    return get_objects(models.Kitten, db)


def get_kitten(kitten_id: int, db: Session):
    return get_object(models.Kitten, kitten_id, db)


def get_kittens_by_breed(breed: str, db: Session):
    return db.execute(
        select(models.Kitten)
        .join(models.Breed)
        .where(models.Breed.name == breed)
    ).scalars().all()


def create_kitten(kitten_data: dict, db: Session):
    kitten_db = models.Kitten(**kitten_data)
    return create_object(kitten_db, db)


def update_kitten(kitten_db: models.Kitten, kitten_data: dict, db: Session):
    return update_object(kitten_db, kitten_data, db)


def delete_kitten(kitten_db: models.Kitten, db: Session):
    delete_object(kitten_db, db)
