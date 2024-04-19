from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def dtype_markup() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text = "температура, °C", callback_data = "temperature")],
                [InlineKeyboardButton(text = "влажность, %", callback_data = "humidity")],
                [InlineKeyboardButton(text = "скорость ветра, м/с", callback_data = "wind_speed")]
                ]
    
    markup = InlineKeyboardMarkup(keyboard = keyboard, row_width = 1)
    return markup
