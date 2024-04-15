from loader import bot
from telebot.types import Message
from states import AskFor
from utils.logging import log_from


@bot.message_handler(commands = ["change_city"])
@log_from
def change_city_cmd(message: Message):
    bot.send_message(message.chat.id,
                     "To let me track weather in your region, please, enter your city name:")
    bot.set_state(message.from_user.id, AskFor.city, message.chat.id)
