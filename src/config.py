from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv

from functools import lru_cache

load_dotenv("dev.env")
load_dotenv("prod.env", override=True)


@final
class Global_config(BaseSettings):

    debug: bool
    redis_url: str
    bot_token: str
    base_webhook_url: str
    webhook_path: str 
    telegram_my_token: str 

    model_config = SettingsConfigDict(
        env_file=None
    )
    

@lru_cache()
def get_config() -> Global_config:
    return Global_config()

