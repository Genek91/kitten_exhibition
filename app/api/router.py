from fastapi import APIRouter

from app.api.endpoints import breed_router, kitten_router

main_router = APIRouter()

main_router.include_router(
    breed_router, prefix="/breeds", tags=["Breed"]
)
main_router.include_router(
    kitten_router, prefix="/kittens", tags=["Kitten"]
)
