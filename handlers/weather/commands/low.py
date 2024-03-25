from telebot.types import Message
from loader import bot
from states import AskFor
from utils.logging import log_from
from keyboards.inline import dtype_markup


@bot.message_handler(commands = ["low"])
@log_from
def low_cmd(message: Message):
    markup = dtype_markup()
    bot.send_message(message.chat.id, "Choose data type:", reply_markup = markup)
    bot.set_state(message.from_user.id, AskFor.dtype, message.chat.id)
