from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache



@final
class Global_config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('prod.env', 'dev.env'),
        env_file_encoding='utf-8'
    )

    debug: bool = True
    redis_url: str
    bot_token: str
    base_webhook_url: str
    webhook_path: str
    telegram_my_token: str
    

@lru_cache()
def get_config() -> Global_config:
    return Global_config()

