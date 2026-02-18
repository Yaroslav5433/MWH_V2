from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..core.database_config import db_config
from sqlalchemy.orm import DeclarativeBase
import asyncio

async_engine = create_async_engine(
    url = db_config.DB_URL_asyncpg,
    echo = True,
)

async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass
