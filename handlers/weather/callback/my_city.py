from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from database import User, Country, City
from utils.logging import log_call


@bot.callback_query_handler(lambda call: not call.data == "<<back", state = AskFor.city)
@log_call
def take_call_city(call: CallbackQuery):
    user: User = User.get(username = call.from_user.username)
    country: Country = Country.get_by_id(user.country_id)
    city_name, lat, lon = call.data.split(",")
    
    try:
        city = City.get(name = city_name, country_id = country.id)
    except City.DoesNotExist:
        city = City(name = city_name, country_id = user.country_id, latitude = lat, longitude = lon)
        city.save()
    user.city_id = city.id
    user.save()
    bot.edit_message_reply_markup(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, f"Good! Now set up to track weather in {city.name}({country.code})")
