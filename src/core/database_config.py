from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

from typing import final

BASE_DIR = Path(__file__).resolve().parent


@final
class DB_Config(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file= BASE_DIR / "db.env"
    )

db_config = DB_Config()



# @lru_cache
# def get_db_config() -> DB_Config:
#     return DB_Config()

# db_config = get_db_config()