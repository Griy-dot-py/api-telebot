from telebot.types import Message
from loader import bot, storage
from database import authorize
from handlers.weather.message import change_city_cmd
from utils.logging import log_from


@bot.message_handler(state = "*", commands = ["cancel"])
@log_from
def cancel_cmd(message: Message):
    text = "Операция отменена" if storage.get_state(message.chat.id, message.from_user.id)is not None \
            else "Нечего отменять ..."
    bot.delete_state(message.from_user.id, message.chat.id)
    msg = bot.send_message(message.chat.id, text)
    
    user = authorize(message.from_user)
    if user.city_id is None:
        bot.edit_message_text(
            "Вы должны указать местоположения, чтобы можно было отслеживать погоду в вашем регионе!",
            msg.chat.id, msg.id
            )
        change_city_cmd(message)
