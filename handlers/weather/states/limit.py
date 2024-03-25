from telebot.types import Message
from loader import bot
from states import AskFor
from utils.logging import log_from
from api import forecast


@bot.message_handler(state = AskFor.limit)
@log_from
def take_limit(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        dtype = data["type"]
        frange = data["range"]
        limit = int(message.text)
    
    # forecast_text = forecast(dtype, frange, limit)
    forecast_text = dtype, frange, limit
    forecast(*forecast_text)
    bot.send_message(message.chat.id, str(forecast_text))
    bot.delete_state(message.from_user.id, message.chat.id)
