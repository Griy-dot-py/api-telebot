from telebot.types import User
from database import City, authorize


def set_user_city(telebot_user: User, name: str) -> None:
    user = authorize(telebot_user)
    city: City = City.get(name = name)
    user.city_id = city.id
    