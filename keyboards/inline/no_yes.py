from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def yes_no(text: str) -> InlineKeyboardMarkup:
    yes = InlineKeyboardButton("Yes", callback_data = f"yes,{text}")
    no = InlineKeyboardButton("No", callback_data = f"no,{text}")
    markup = InlineKeyboardMarkup([[yes, no]], row_width = 2)
    return markup
