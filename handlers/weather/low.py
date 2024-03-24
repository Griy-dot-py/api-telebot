from telebot.types import Message
from loader import bot
from utils.log_messages import log_from
from keyboards.inline.data_type import data_type


@bot.message_handler(commands = ["low"])
@log_from
def low(message: Message):
    markup = data_type()
    bot.send_message(message.chat.id, "Choose data type:", reply_markup = markup)
