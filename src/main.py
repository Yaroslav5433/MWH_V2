from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger
from database import create_db_engine

import src.tg_bot.handlers
from .routes.tg_routes import root_router
from .tg_bot.bot import start_telegram

@asynccontextmanager
async def lifespan(application: FastAPI):
    logger.info("Starting Application")
    await create_db_engine()
    await start_telegram()
    yield
    logger.info("Stopping Application")

app = FastAPI(lifespan=lifespan)
app.include_router(root_router)