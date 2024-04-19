from loader import bot
from telebot.types import Message
from states import AskFor
from api import geolocation
from keyboards.inline import city_variants
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.city, valid_city = "soft")
@log_from
def take_city(message: Message):
    variants = geolocation(message.text, all = True)
    bot.send_message(
        message.chat.id,
        "Не могу найти такой город, может вы имели ввиду один из списка:",
        reply_markup = city_variants(variants)
        )