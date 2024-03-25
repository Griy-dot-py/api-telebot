from telebot.types import Message
from loader import bot
from database import City, User
from api import current_weather
from utils.logging import log_from


@bot.message_handler(commands = ["current"])
@log_from
def current_cmd(message: Message):
    user: User = User.get(username = message.from_user.username)
    city: City = City.get_by_id(user.city_id)
    
    weather = current_weather(city.latitude, city.longitude)
    bot.send_message(message.chat.id, weather)
