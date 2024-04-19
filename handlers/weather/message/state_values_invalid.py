from telebot.types import Message
from loader import bot
from states import AskFor
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.values, valid_values = False)
@log_from
def take_invalid_values(message: Message):
    bot.reply_to(message, "Пожалуйста, введите только 2 числа")
