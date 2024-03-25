from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from utils.logging import log_call


@bot.callback_query_handler(func = lambda call: True, state = AskFor.frange)
@log_call
def take_frange(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data["range"] = call.data
    bot.edit_message_text("Now write limit of values to show:",
                          call.message.chat.id, call.message.id)
    bot.set_state(call.from_user.id, AskFor.limit, call.message.chat.id)
