from loader import bot
from telebot.types import Message
from states import AskFor
from api import search_by_name
from keyboards.inline import yes_no
from utils.logging import log_from


@bot.message_handler(state = AskFor.country, valid_country = "soft")
@log_from
def take_country(message: Message):
    code, country = search_by_name(message.text)
    bot.send_message(message.chat.id, f"Cannot find this country, maybe you meant {country}({code})?",
                     reply_markup = yes_no(country))
