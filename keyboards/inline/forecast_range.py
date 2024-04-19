from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def frange_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text = "на сегодня", callback_data = "today")],
        [InlineKeyboardButton(text = "на завтра", callback_data = "tomorrow")],
        [InlineKeyboardButton(text = "ближайшие 5 дней", callback_data = "next_5_days")]
    ]
    
    markup = InlineKeyboardMarkup(keyboard = keyboard, row_width = 1)
    return markup
