from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROD_DATABASE_URL: Optional[str] = None
    TEST_DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
