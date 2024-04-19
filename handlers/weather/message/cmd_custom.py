from telebot.types import Message
from loader import bot
from database import User
from handlers.weather.message import change_city_cmd
from states import AskFor
from utils.logging import log_from
from keyboards.inline import dtype_markup


@bot.message_handler(commands = ["custom"])
@log_from
def custom_cmd(message: Message):
    user: User = User.get(username = message.from_user.username)
    if user.city_id is None:
        change_city_cmd(message)
        return
    
    markup = dtype_markup()
    bot.send_message(message.chat.id, "Выберите показатель:", reply_markup = markup)
    bot.set_state(message.from_user.id, AskFor.dtype, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["desc"] = None
        data["custom"] = True
