from telebot.types import Message
from loader import bot
from database import User
from handlers.weather.commands import change_city_cmd
from utils.logging import log_from


@bot.message_handler(state = None, commands = ["cancel"])
@log_from
def useless_cancel_cmd(message: Message):
    bot.send_message(message.chat.id, "I wasn't do anything anyway...")
