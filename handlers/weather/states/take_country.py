from loader import bot
from telebot.types import Message
from states import AskFor
from database import Country, User
from api import search_by_name
from utils.logging import log_from


@bot.message_handler(state = AskFor.country)
@log_from
def take_country(message: Message):
    try:
        country: Country | None = Country.get(name = message.text)
    except Country.DoesNotExist:
        common, code = search_by_name(message.text)
        try:
            country: Country | None = Country.get(code = code)
        except Country.DoesNotExist:
            country = Country(name = common, code = code)
            country.save()
    
    user: User = User.get(username = message.from_user.username)
    user.country_id = country.id
    user.save()

    bot.send_message(message.chat.id, "Now enter your city name:")
    bot.set_state(message.from_user.id, AskFor.city, message.chat.id)
