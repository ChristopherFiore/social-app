# Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPI app setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic health checks for api
@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# DB TESTING, Remove after
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        return {"db": "connected"}
