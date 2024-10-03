from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database import Base


class Breed(Base):

    __tablename__ = "breeds"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    kittens: Mapped[list["Kitten"]] = relationship(
        "Kitten", cascade="all, delete", back_populates="breed"
    )


class Kitten(Base):

    __tablename__ = "kittens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    color: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)

    breed_id: Mapped[int] = mapped_column(Integer, ForeignKey("breeds.id"))
    breed: Mapped["Breed"] = relationship("Breed", back_populates="kittens")
