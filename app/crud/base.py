from sqlalchemy.orm import Session
from sqlalchemy.future import select


def get_objects(model, db: Session):
    return db.execute(select(model)).scalars().all()


def get_object(model, id: int, db: Session):
    return db.execute(
        select(model).where(model.id == id)
    ).scalar_one_or_none()


def create_object(obj, db: Session):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_object(obj, data: dict, db: Session):
    for key, value in data.items():
        setattr(obj, key, value)
    db.commit()
    return obj


def delete_object(obj, db: Session):
    db.delete(obj)
    db.commit()
