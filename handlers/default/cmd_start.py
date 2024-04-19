from telebot.types import Message
from loader import bot
from handlers.weather.message import change_city_cmd
from handlers.default import help_cmd
from database import User
from utils.logging import log_from


@bot.message_handler(commands = ["start"])
@log_from
def start_cmd(message: Message):
    try:
        User.get(username = message.from_user.username)
    except User.DoesNotExist:
        new = User(username = message.from_user.username)
        new.save()
    
    bot.send_message(message.chat.id, "Здравствуйте! Я помогу вам узнать прогноз погоды")
    help_cmd(message)
    change_city_cmd(message)
