from loader import bot
from telebot.types import Message
from states import AskFor
from database import User, City
from utils.logging import log_from


@bot.message_handler(state = AskFor.city, valid_city = "hard")
@log_from
def take_valid_city(message: Message):
    user: User = User.get(username = message.from_user.username)
    city: City = City.get(name = message.text)
    user.city_id = city.id
    user.save()
    
    bot.send_message(
        message.chat.id,
        f"Отлично! Теперь я отслеживаю погоду в городе {city.name}({city.country})")
    bot.delete_state(message.from_user.id, message.chat.id)
