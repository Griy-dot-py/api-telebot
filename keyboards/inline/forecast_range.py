from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def forecast_range(datatype: str) -> InlineKeyboardMarkup:
    callback = "{\"data\": \"" + datatype+ "\", \"range\": \"%s\"}"
    today = InlineKeyboardButton("today", callback_data = callback % "today")
    tomorr = InlineKeyboardButton("tomorrow", callback_data = callback % "tomorrow")
    next_5 = InlineKeyboardButton("next 5 days", callback_data = callback  % "next_5_days")
    markup = InlineKeyboardMarkup(row_width = 1)
    markup.add(today, tomorr, next_5)
    return markup
