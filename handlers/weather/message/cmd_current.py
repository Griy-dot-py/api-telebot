from telebot.types import Message
from loader import bot
from database import get_user_city
from api import current_weather
from handlers.weather.message import change_city_cmd


@bot.message_handler(commands = ["current"])
def current_cmd(message: Message):
    city = get_user_city(message.from_user)
    if city is None:
        change_city_cmd(message)
        return
    
    weather = current_weather(city)
    bot.send_message(message.chat.id, weather)
