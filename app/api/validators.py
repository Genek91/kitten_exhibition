from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud import breed_crud, kitten_crud


def check_breed(breed_id: int, db: Session):
    breed = breed_crud.get_breed(breed_id, db)
    if breed is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Порода не найдена"
        )
    return breed


def check_unique_breed(breed: str, db: Session):
    breed = breed_crud.get_breed_by_name(breed, db)
    if breed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Порода уже существует"
        )
    return breed


def check_kitten(kitten_id: int, db: Session):
    kitten = kitten_crud.get_kitten(kitten_id, db)
    if kitten is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Котёнок не найден"
        )
    return kitten
