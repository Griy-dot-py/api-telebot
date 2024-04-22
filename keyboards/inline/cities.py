from typing import Iterator
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import City


def city_variants(cities: list[City]) -> InlineKeyboardMarkup:
    keyboard = [[button] for button in __button_gen(cities)]
    
    markup = InlineKeyboardMarkup(keyboard = keyboard, row_width = 1)
    return markup


def __button_gen(cities: list[City]) -> Iterator[InlineKeyboardButton]:
    for city in cities:
        button = InlineKeyboardButton(
            text = f"{city.name}({city.country})",
            callback_data = f"{city.id}"
        )
        yield button
