from telebot.types import Message
from loader import bot


@bot.message_handler(commands = ["hello_world"])
def hello_world(message: Message):
    bot.send_message(message.chat.id, "Hello, world!")
