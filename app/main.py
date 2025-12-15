from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, schemas, crud
from fastapi.responses import RedirectResponse
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="URL Shortener Service",
    description="Backend service for shortening URLs",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(
    request: schemas.URLCreate,
    db: Session = Depends(get_db)
):
    url = crud.create_short_url(db, str(request.original_url))

    short_url = f"{settings.base_url}/{url.short_code}"

    return {
        "short_url": short_url
    }


@app.get("/{short_code}")
def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = crud.get_url_by_short_code(db, short_code)

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(
        url=url.original_url,
        status_code=302
    )
