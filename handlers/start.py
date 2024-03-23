from telebot.types import Message
from loader import bot


@bot.message_handler(commands = ["start"])
def starting(message: Message):
    bot.send_message(message.chat.id, "Hello! Now I can only greet you and repeat your messages")
