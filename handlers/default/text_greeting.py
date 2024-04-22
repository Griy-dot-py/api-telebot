from telebot.types import Message
from loader import bot


@bot.message_handler(func = lambda message: message.text.lower() in ["привет", "hi", "ку"])
def greeting(message: Message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.full_name}!")
