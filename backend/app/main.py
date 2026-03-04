from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base
from app.api import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "API running"}
