from telebot.types import Message
from loader import bot
from database import City, User
from api import current_weather
from utils.logging import log_from
from handlers.weather.message import change_city_cmd


@bot.message_handler(commands = ["current"])
@log_from
def current_cmd(message: Message):
    user: User = User.get(username = message.from_user.username)
    if user.city_id is None:
        change_city_cmd(message)
        return
    
    weather = current_weather(City.get_by_id(user.city_id))
    bot.send_message(message.chat.id, weather)
