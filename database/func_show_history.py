from telebot.types import User
import pickle
from database import authorize


def show_history(telebot_user: User) -> list[str]:
    user = authorize(telebot_user)
    return pickle.loads(user.history)
