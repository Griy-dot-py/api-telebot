from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def city_variants(variants: list) -> InlineKeyboardMarkup:
    cities = [
        [InlineKeyboardButton(name, callback_data = f"{name},{lat},{lon}")] for name, lat, lon in variants
        ]
    cities.append([InlineKeyboardButton("<< Back to country choice", callback_data = "<<back")])
    markup = InlineKeyboardMarkup(keyboard = cities, row_width = 1)
    return markup
