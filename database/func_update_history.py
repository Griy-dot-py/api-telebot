from telebot.types import Message
import pickle
from database import authorize, show_history


def update_history(message: Message) -> None:
    user = authorize(message.from_user)
    history = show_history(message.from_user)
    history.insert(0, message.text)
    user.history = pickle.dumps(history[: 10])
    user.save()
    