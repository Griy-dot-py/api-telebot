from telebot.types import Message
from loader import bot
from states import AskFor
from utils import two_floats
from utils.logging import log_from


@bot.message_handler(no_cmd = True, state = AskFor.values, valid_values = True)
@log_from
def take_values(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["custom_values"] = two_floats(message.text)
    
    bot.send_message(message.chat.id, "Теперь напишите число значений, которые нужно показать:")
    bot.set_state(message.from_user.id, AskFor.limit, message.chat.id)
