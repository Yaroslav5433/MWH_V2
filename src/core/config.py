from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache


@final
class Global_config(BaseSettings):

    debug: bool
    redis_url: str
    bot_token: str
    base_webhook_url: str
    webhook_path: str 
    telegram_my_token: str 

    model_config = SettingsConfigDict(
        env_file="dev.env"
    )
    

@lru_cache()
def get_config() -> Global_config:
    return Global_config()

