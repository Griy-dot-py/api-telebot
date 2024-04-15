from telebot.types import Message
from loader import bot, storage
from database import User
from handlers.weather.message import change_city_cmd
from utils.logging import log_from


@bot.message_handler(state = "*", commands = ["cancel"])
@log_from
def cancel_cmd(message: Message):
    text = "Opearation cancelled" if storage.get_state(message.chat.id, message.from_user.id)is not None \
            else "I wasn't doing anything anyway..."
    bot.delete_state(message.from_user.id, message.chat.id)
    msg = bot.send_message(message.chat.id, text)
    
    user: User = User.get(username = message.from_user.username)
    if user.city_id is None:
        bot.edit_message_text("You must share your location so I can track weather in your region!",
                              msg.chat.id, msg.id)
        change_city_cmd(message)
