from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def data_type() -> InlineKeyboardMarkup:
    callback = "{\"data\": \"%s\"}"
    temp = InlineKeyboardButton("temperature", callback_data = callback % "temp")
    hum = InlineKeyboardButton("humidity", callback_data = callback % "humidity")
    ws = InlineKeyboardButton("wind speed", callback_data = callback % "wind_speed")
    markup = InlineKeyboardMarkup(row_width = 1)
    markup.add(temp, hum, ws)
    return markup
