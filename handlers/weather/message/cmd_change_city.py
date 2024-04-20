from loader import bot
from telebot.types import Message
from states import AskFor


@bot.message_handler(commands = ["change_city"])
def change_city_cmd(message: Message):
    bot.send_message(message.chat.id,
                     "Чтобы можно было отслеживать погоду, пожалуйста введите ваш город:")
    bot.set_state(message.from_user.id, AskFor.city, message.chat.id)
