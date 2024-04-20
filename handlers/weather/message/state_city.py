from loader import bot
from telebot.types import Message
from states import AskFor
from api import geolocation
from database import set_ids_for_cities
from keyboards.inline import city_variants


@bot.message_handler(no_cmd = True, state = AskFor.city, valid_city = "soft")
def take_city(message: Message):
    possible_cities = geolocation(message.text)
    cities_with_ids = set_ids_for_cities(possible_cities)
        
    bot.send_message(
        message.chat.id,
        "Не могу найти такой город, может вы имели ввиду один из списка:",
        reply_markup = city_variants(cities_with_ids)
        )
