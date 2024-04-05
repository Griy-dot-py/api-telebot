from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def dtype_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(dtype.replace("_", " "), callback_data = dtype)]
        for dtype in ("temperature", "humidity", "wind_speed")
    ]
    markup = InlineKeyboardMarkup(keyboard = keyboard, row_width = 1)
    return markup
