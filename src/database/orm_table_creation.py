from src.database.database import async_engine
from src.database.db_models import Base
from sqlalchemy import inspect
import asyncio


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())