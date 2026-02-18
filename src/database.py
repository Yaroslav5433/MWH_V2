from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from core.database_config import db_config
import asyncio

engine = create_async_engine(
    url = db_config.DB_URL_asyncpg,
    echo = True,
)

async def create_db_engine():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res}")
