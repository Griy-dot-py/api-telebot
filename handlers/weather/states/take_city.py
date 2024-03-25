from loader import bot
from telebot.types import Message
from states import AskFor
from database import Country, User, City
from api import geolocation
from utils.logging import log_from


@bot.message_handler(state = AskFor.city)
@log_from
def take_city(message: Message):
    user: User = User.get(username = message.from_user.username)
    country: Country = Country.get(id = user.country_id)
    
    try:
        city: City | None = City.get(name = message.text, country_id = country.id)
    except City.DoesNotExist:
        common, lat, lon = geolocation(message.text, country.code)
        try:
            city: City | None = City.get(latitude = lat, longitude = lon)
        except City.DoesNotExist:
            city = City(name = common, country_id = country.id, latitude = lat, longitude = lon)
            city.save()
    
    user.city_id = city.id
    user.save()
    
    bot.send_message(
        message.chat.id,
        f"Good! Now set up to track weather in {city.name}, {country.code}")
    bot.delete_state(message.from_user.id, message.chat.id)

