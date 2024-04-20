from telebot.types import User as TeleUser
from database import User


def authorize(telebot_user: TeleUser) -> User:
    user, *_ = User.get_or_create(username = telebot_user.username)
    return user