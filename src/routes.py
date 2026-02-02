from typing import Annotated

from fastapi import APIRouter, Header
from loguru import logger
from aiogram import types

from bot import bot, dp
from config import get_config

cfg = get_config()

root_router = APIRouter(
    prefix="",
    tags=['root'],
    responses={404: {"description": "Not Found"}},
)

@root_router.get("/")
async def root() -> dict:
    return {"message": "Hello world!"}

