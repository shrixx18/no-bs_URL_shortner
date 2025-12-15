import string
import random
from sqlalchemy.orm import Session
from . import models

SHORT_CODE_LENGTH = 6
CHARSET = string.ascii_letters + string.digits


def generate_short_code() -> str:
    return ''.join(random.choices(CHARSET, k=SHORT_CODE_LENGTH))


def normalize_url(url: str) -> str:
    return url.rstrip("/")


def create_short_url(db: Session, original_url: str) -> models.URL:
    normalized_url = normalize_url(original_url)

    # Check if URL already exists
    existing = db.query(models.URL).filter(
        models.URL.original_url == normalized_url
    ).first()

    if existing:
        return existing

    while True:
        short_code = generate_short_code()

        collision = db.query(models.URL).filter(
            models.URL.short_code == short_code
        ).first()

        if not collision:
            break

    url = models.URL(
        original_url=normalized_url,
        short_code=short_code
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url


def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(
        models.URL.short_code == short_code
    ).first()
