from loader import bot
from telebot.types import Message
from states import AskFor
from database import Country, User
from utils.logging import log_from


@bot.message_handler(state = AskFor.country, valid_country = "hard")
@log_from
def take_valid_country(message: Message):
    user: User = User.get(username = message.from_user.username)
    country: Country = Country.get(name = message.text)
    user.country_id = country.id
    user.save()

    bot.send_message(message.chat.id, "Now enter your city name:")
    bot.set_state(message.from_user.id, AskFor.city, message.chat.id)
