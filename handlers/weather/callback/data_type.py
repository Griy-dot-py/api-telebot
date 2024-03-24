from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline.forecast_range import forecast_range
import json


@bot.callback_query_handler(func = lambda call: call.data.startswith("{") and len(json.loads(call.data)) == 1)
def data_type_handler(call: CallbackQuery):
    call_data = json.loads(call.data)
    bot.edit_message_text("Now choose forecast range:", call.message.chat.id, call.message.id, 
                          reply_markup = forecast_range(call_data["data"]))
