from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from utils.logging import log_call


@bot.callback_query_handler(lambda call: call.data == "<<back", state = AskFor.city)
@log_call
def take_no_city(call: CallbackQuery):
    bot.edit_message_reply_markup(call.message.chat.id,
                                  call.message.id)
    bot.send_message(call.message.chat.id,
                     "To let me track weather in your region, please, enter your country name:")
    bot.set_state(call.from_user.id, AskFor.country, call.message.chat.id)
