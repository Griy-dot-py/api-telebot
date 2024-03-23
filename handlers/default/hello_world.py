from telebot.types import Message
from loader import bot
from utils.log_messages import log_from


@bot.message_handler(commands = ["hello_world"])
@log_from
def hello_world(message: Message):
    bot.send_message(message.chat.id, "Hello, world!")
