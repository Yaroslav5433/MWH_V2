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
    redis_url: str = 'redis://localhost:6379/0'
    bot_token: str = '7852065328:AAFNPKUvuZ0TswVrrdpf3zIKWoTRadjgHis'
    base_webhook_url: str = 'https://hydrogeologic-unelegant-finnegan.ngrok-free.dev'
    webhook_path: str = '/telegram/webhook'
    telegram_my_token: str = '3u487u38asdbf012ndmc9f'
    

@lru_cache()
def get_config() -> Global_config:
    return Global_config()

