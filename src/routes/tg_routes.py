from typing import Annotated

from fastapi import APIRouter, Header
from loguru import logger
from aiogram import types

from .bot import bot, dp
from .config import get_config

cfg = get_config()

root_router = APIRouter(
    prefix="",
    tags=['root'],
    responses={404: {"description": "Not Found"}},
)

@root_router.get("/")
async def root() -> dict:
    return {"message": "Hello world!"}

@root_router.post(cfg.webhook_path)
async def bot_webhook(update: dict,
                      x_telegram_bot_api_secret_token: Annotated[str | None, Header()] = None) -> None | dict:
    if x_telegram_bot_api_secret_token != cfg.telegram_my_token:
        logger.error("Wrong secret token!")
        return {"status": "error", "message": "Wrong secret token"}
    telegram_update = types.Update(**update)
    return await dp.feed_webhook_update(bot=bot, update=telegram_update)
    
    