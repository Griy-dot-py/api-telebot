from telebot.types import Message
from loader import bot
from states import AskFor
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.limit, is_digit = False)
@log_from
def take_incorrect_limit(message: Message):
    bot.reply_to(message, "Пожалуйста, введите одно целое число!")
