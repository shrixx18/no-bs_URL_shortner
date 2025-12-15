from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql://postgres:1827@localhost/nobs'
    base_url: str = "http://localhost:8000"

    class Config:
        env_file = ".env"


settings = Settings()
