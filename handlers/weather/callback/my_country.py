from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from database import User, Country
from utils.logging import log_call


@bot.callback_query_handler(lambda call: call.data.startswith("yes"), state = AskFor.country)
@log_call
def take_call_country(call: CallbackQuery):
    user: User = User.get(username = call.from_user.username)
    country: Country = Country.get(name = call.data.split(",")[1])
    user.country_id = country
    user.save()
    
    bot.edit_message_reply_markup(call.message.chat.id,
                                  call.message.id)
    bot.send_message(call.message.chat.id, "Now enter your city name:")
    bot.set_state(call.from_user.id, AskFor.city, call.message.chat.id)
