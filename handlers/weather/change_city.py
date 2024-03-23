from loader import bot
from telebot.types import Message
from states.ask_for import AskFor

from database.model_place import Country, City
from database.model_user import User

from api import restcountries, open_weather


@bot.message_handler(commands = ["change_city"])
def change_city(message: Message):
    bot.send_message(message.chat.id, "Please, enter your country name:")
    bot.set_state(message.from_user.id, AskFor.country, message.chat.id)


@bot.message_handler(state = AskFor.country)
def take_country(message: Message):
    try:
        country: Country | None = Country.get(name = message.text)
    except Country.DoesNotExist:
        common, code = restcountries.name(message.text)
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
   

@bot.message_handler(state = AskFor.city)
def take_city(message: Message):
    user: User = User.get(username = message.from_user.username)
    country: Country = Country.get(id = user.country_id)
    
    try:
        city: City | None = City.get(name = message.text, country_id = country.id)
    except City.DoesNotExist:
        common, lat, lon = open_weather.geo(message.text, country.code)
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
