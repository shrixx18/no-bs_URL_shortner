from fastapi import FastAPI
from app.database import engine
from app import models


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="URL Shortener Service",
    description="Backend service for shortening URLs",
    version="1.0.0"
)


@app.get("/")
def welcome():
    return {
        "Message": "Welcome to the home page"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "url-shortener"
    }
