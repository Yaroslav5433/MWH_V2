from loguru import logger
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import bold
from aiogram.types import Message
from aiogram.enums import ParseMode

from src.tg_bot.handlers import keyboards
from src.tg_bot.bot import telegram_router
from src.database.orm import create_user


@telegram_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"""
    Hello, {bold(message.from_user.full_name)}!,
This bot was specially design for Hyatt Regency Pravets Resort
If you're reading this - you're now part of our big family
To proceed further - choose one of the active functions below:""",
    reply_markup=keyboards.start_keyboard,
    parse_mode=ParseMode.MARKDOWN)

    await create_user(
        tg_username = message.from_user.username,
        tg_user_id = message.from_user.id
    )
    
