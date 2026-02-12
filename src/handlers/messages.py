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


@telegram_router.message(F.text == "Sent a request for a day's off for a next week")
async def sent_desirable_day_off(message: types.Message) -> None:
    pass


@telegram_router.message(F.text == "Sent an anonymous message to a manager")
async def sent_anonymous_message(message: types.Message) -> None:
    pass


@telegram_router.message(F.text == "More information about bot")
async def sent_info_about_bot(message: types.Message) -> None:
    await message.answer(
        """
MyWorkingHours Bot is a smart assistant designed to simplify communication between managers and employees and automate everyday workflow processes.

With this bot, employees can:
📅 View their personal work schedule anytime
🔄 Submit requests to change their working hours
📝 Send complaints or feedback directly to management
👀 Check updated shifts in real time

The bot works together with the MyManager platform, where managers create and manage schedules, assign departments, and instantly distribute work hours to employees with just one click.

MyManager Bot makes routine processes faster, more convenient, and more efficient for everyone."
""",
        reply_markup=keyboards.start_keyboard_without_info
    )


@telegram_router.message(F.text == "Get back to the main menu")
async def sent_anonymous_message(message: types.Message) -> None:
    await message.answer(
        "Choose one of the next actions:",
        reply_markup=keyboards.start_keyboard
    )