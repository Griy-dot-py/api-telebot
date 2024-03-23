from telebot.types import Message
from loader import bot
from handlers.weather.change_city import change_city
from database.model_user import User


@bot.message_handler(commands = ["start"])
def starting(message: Message):
    try:
        User.get(username = message.from_user.username)
    except User.DoesNotExists:
        new = User(username = message.from_user.username)
        new.save()
    
    bot.send_message(message.chat.id, "Hello! Now I can only greet you")
    change_city(message)
