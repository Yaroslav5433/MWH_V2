from loguru import logger
from aiogram import types
from aiogram import F
from aiogram.utils.markdown import bold

from src.handlers import keyboards
from src.bot import telegram_router


@telegram_router.message(F.text == "Interaction with my working hours")
async def crud_hours(message: types.Message) -> None:
    await message.answer(
        "Choose what you want to do with your hours:",
        reply_markup=keyboards.hours_interaction_keyboard
    )


@telegram_router.message(F.text == "Choose a desirable day's off for a next week")
async def sent_desirable_day_off(message: types.Message) -> None:
    pass


@telegram_router.message(F.text == "Sent an anonymous message to a manager")
async def sent_anonymous_message(message: types.Message) -> None:
    pass


@telegram_router.message(F.text == "More information about bot")
async def sent_info_about_bot(message: types.Message) -> None:
    await message.answer(
        "Here would be an info with all functions",
        reply_markup=keyboards.start_keyboard_without_info
    )

