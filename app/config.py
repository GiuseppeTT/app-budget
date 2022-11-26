from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLITE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
