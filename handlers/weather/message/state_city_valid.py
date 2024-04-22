from loader import bot
from telebot.types import Message
from states import AskFor
from database import get_user_city, set_user_city


@bot.message_handler(no_cmd = True, state = AskFor.city, valid_city = "hard")
def take_valid_city(message: Message):
    set_user_city(message.from_user, message.text)
    city = get_user_city(message.from_user)
    
    bot.send_message(
        message.chat.id,
        f"Отлично! Теперь я отслеживаю погоду в городе {city.name}({city.country})")
    bot.delete_state(message.from_user.id, message.chat.id)
