from fastapi import FastAPI

from app.api.router import main_router
from app.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(main_router)
