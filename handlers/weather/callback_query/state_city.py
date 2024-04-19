from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from database import User, City
from utils.logging import log_call


@bot.callback_query_handler(func = lambda call: True, state = AskFor.city)
@log_call
def take_call_city(call: CallbackQuery):
    user: User = User.get(username = call.from_user.username)
    city_name, country, lat, lon = call.data.split(",")
    
    try:
        city = City.get(name = city_name, country = country)
    except City.DoesNotExist:
        city = City(name = city_name, country = country, latitude = lat, longitude = lon)
        city.save()
    user.city_id = city.id
    user.save()
    bot.edit_message_reply_markup(call.message.chat.id, call.message.id)
    bot.send_message(
        call.message.chat.id, 
        f"Отлично! Теперь я отслеживаю погоду в городе {city.name}({city.country})"
        )
    bot.delete_state(call.from_user.id, call.message.chat.id)