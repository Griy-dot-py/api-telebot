from telebot.types import Message
from loader import bot
from states import AskFor
from classes import Forecast


@bot.message_handler(no_cmd = True, state = AskFor.limit, valid_limit = True)
def take_limit(message: Message):
    forecast = Forecast(message = message, bot = bot)
    forecast.update()
    
    bot.send_message(message.chat.id, forecast.complete())
    bot.delete_state(message.from_user.id, message.chat.id)
