from telebot.types import Message
from loader import bot

from database.model_user import User
from database.model_place import City

from api import open_weather


@bot.message_handler(commands = ["current"])
def current(message: Message):
    user: User = User.get(username = message.from_user.username)
    city: City = City.get_by_id(user.city_id)
    
    weather = open_weather.current(city.latitude, city.longitude)
    bot.send_message(message.chat.id, weather)
