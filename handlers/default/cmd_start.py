from telebot.types import Message
from loader import bot
from handlers.weather.message import change_city_cmd
from handlers.default import help_cmd
from database import authorize


@bot.message_handler(commands = ["start"])
def start_cmd(message: Message):
    authorize(message.from_user)
    
    bot.send_message(message.chat.id, "Здравствуйте! Я помогу вам узнать прогноз погоды")
    help_cmd(message)
    change_city_cmd(message)
