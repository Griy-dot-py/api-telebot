from telebot.types import Message
from loader import bot
from utils.logging import log_from


@bot.message_handler(func = lambda message: message.text.lower() in ["привет", "hi", "ку"])
@log_from
def greeting(message: Message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.full_name}!")
