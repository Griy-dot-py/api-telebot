from telebot.types import User as TeleUser
from database import City
from database import authorize


def get_user_city(telebot_user: TeleUser) -> City:
    user = authorize(telebot_user)
    if user.city_id is None:
        return None
    return City.get_by_id(user.city_id)
