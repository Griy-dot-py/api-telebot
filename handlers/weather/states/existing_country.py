from loader import bot
from telebot.types import Message
from states import AskFor
from utils.logging import log_from


@bot.message_handler(state = AskFor.country, valid_country = "soft")
@log_from
def take_existing_country(message: Message):
    bot.send_message(message.chat.id, "This country added to database")
