from telebot.types import Message
from loader import bot
from states import AskFor


@bot.message_handler(no_cmd = True, state = AskFor.values, valid_values = False)
def take_invalid_values(message: Message):
    bot.reply_to(message, "Пожалуйста, введите только 2 числа")
