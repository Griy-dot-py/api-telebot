from loader import bot
from telebot.types import Message
from states import AskFor
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.city, valid_city = "etc")
@log_from
def take_incorrect_city(message: Message):
    bot.send_message(message.chat.id, "Cannot find such city on Earth")
