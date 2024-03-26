from loader import bot
from telebot.types import Message
from states import AskFor
from database import Country, User, City
from utils.logging import log_from


@bot.message_handler(state = AskFor.city, valid_city = "hard")
@log_from
def take_city(message: Message):
    user: User = User.get(username = message.from_user.username)
    country: Country = Country.get_by_id(user.country_id)
    city: City = City.get(name = message.text)
    user.city_id = city.id
    user.save()
    
    bot.send_message(
        message.chat.id,
        f"Good! Now set up to track weather in {city.name}, {country.code}")
    bot.delete_state(message.from_user.id, message.chat.id)
