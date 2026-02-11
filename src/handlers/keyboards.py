from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text="Interaction with my working hours")],
    [KeyboardButton(text="Choose a desirable day's off for a next week")],
    [KeyboardButton(text="Sent an anonymous message to a manager")],
    [KeyboardButton(text="More information about bot")]
    ],
    resize_keyboard=True
)


start_keyboard_without_info = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text="Interaction with my working hours")],
    [KeyboardButton(text="Choose a desirable day's off for a next week")],
    [KeyboardButton(text="Sent an anonymous message to a manager")]
    ],
    resize_keyboard=True
)


hours_interaction_keyboard = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text="Save my working hours"), KeyboardButton(text="Change my working hours")],
    [KeyboardButton(text="Delete my working hours"), KeyboardButton(text="Check my working hours")],
    [KeyboardButton(text="Get back to the main menu")]
    ],
    resize_keyboard=True
)

