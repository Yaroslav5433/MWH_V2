from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger
from routes import root_router

@asynccontextmanager
async def lifespan(application: FastAPI):
    logger.info("Starting Application")
    from bot import start_telegram
    await start_telegram()
    yield
    logger.info("Stopping Application")

app = FastAPI(lifespan=lifespan)
app.include_router(root_router)