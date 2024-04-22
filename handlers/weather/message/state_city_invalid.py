from loader import bot
from telebot.types import Message
from states import AskFor


@bot.message_handler(no_cmd = True, state = AskFor.city, valid_city = "etc")
def take_invalid_city(message: Message):
    bot.send_message(message.chat.id, "К сожалению, мне не удалось найти такой город :(")
