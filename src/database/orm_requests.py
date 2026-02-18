from src.database.database import async_session_factory
from src.database.db_models import Mwh_users
from sqlalchemy import select
from aiogram.types import message

async def create_user(tg_username, tg_user_id):
    new_user = Mwh_users(
        username = tg_username,
        tg_id = tg_user_id,
        role = None
    )
    async with async_session_factory() as session:
        session.add(new_user)
        await session.commit()

async def check_user_existence(tg_user_id):
    async with async_session_factory() as session:
        result = await session.execute(
            select(Mwh_users).where(Mwh_users.tg_id == tg_user_id)
        )
        user = result.scalar_one_or_none()
        return user is not None
