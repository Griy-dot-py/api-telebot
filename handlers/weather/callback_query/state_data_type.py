from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from keyboards.inline import frange_markup
from utils.logging import log_call


@bot.callback_query_handler(func = lambda call: True, state = AskFor.dtype)
@log_call
def callback_data_type(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:        
        data["type"] = call.data
    bot.edit_message_text("Выберите тип прогноза:",
                          call.message.chat.id, call.message.id, 
                          reply_markup = frange_markup())
    bot.set_state(call.from_user.id, AskFor.frange, call.message.chat.id)
