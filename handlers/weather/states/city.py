from loader import bot
from telebot.types import Message
from states import AskFor
from api import geolocation
from database import User
from keyboards.inline import city_variants
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.city, valid_city = "soft")
@log_from
def take_city(message: Message):
    user: User = User.get(username = message.from_user.username)
    variants = geolocation(message.text, user.country_id, all = True)
    bot.send_message(message.chat.id, "Cannot find such city, maybe you meant one of this:",
                     reply_markup = city_variants(variants))
