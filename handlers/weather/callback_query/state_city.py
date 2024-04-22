from telebot.types import CallbackQuery
from loader import bot
from states import AskFor
from database import authorize, get_city_by_id


@bot.callback_query_handler(func = lambda call: True, state = AskFor.city)
def take_call_city(call: CallbackQuery):
    city = get_city_by_id(int(call.data))
    user = authorize(call.from_user)
    user.city_id = city.id
    user.save()
    
    bot.edit_message_reply_markup(call.message.chat.id, call.message.id)
    bot.send_message(
        call.message.chat.id, 
        f"Отлично! Теперь я отслеживаю погоду в городе {city.name}({city.country})"
        )
    bot.delete_state(call.from_user.id, call.message.chat.id)
