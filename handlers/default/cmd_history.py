from telebot.types import Message
from loader import bot
from database import show_history


@bot.message_handler(commands = ["history"])
def history_cmd(message: Message):
    history = show_history(message.from_user)
    title = "Ваша краткая история запросов:"
    bot.send_message(message.chat.id, "\n".join([title, *history]))
