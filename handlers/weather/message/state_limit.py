from telebot.types import Message
from loader import bot
from states import AskFor
from classes import Forecast
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.limit, valid_limit = True)
@log_from
def take_limit(message: Message):
    forecast = Forecast(message = message, bot = bot)
    forecast.update()
    
    bot.send_message(message.chat.id, forecast.complete())
    bot.delete_state(message.from_user.id, message.chat.id)
