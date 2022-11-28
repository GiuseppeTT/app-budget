from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROD_DB_URL: Optional[str] = None
    TEST_DB_URL: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
