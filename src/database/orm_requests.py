from src.database.database import async_session_factory
from src.database.db_models import Mwh_users
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