from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def frange_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(frange.replace("_", " "), callback_data = frange)]
        for frange in ("today", "tomorrow", "next_5_days")
    ]
    markup = InlineKeyboardMarkup(keyboard = keyboard, row_width = 1)
    return markup
