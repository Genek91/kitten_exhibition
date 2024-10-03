from pydantic import BaseModel, Field


class BreedBase(BaseModel):

    name: str


class BreedCreate(BreedBase):

    pass


class Breed(BreedBase):

    id: int

    class ConfigDict:
        from_attributes = True


class KittenBase(BaseModel):

    name: str
    color: str
    age: int = Field(..., gt=0)
    description: str
    breed_id: int


class KittenCreate(KittenBase):

    pass


class Kitten(KittenBase):

    id: int

    class ConfigDict:
        from_attributes = True
