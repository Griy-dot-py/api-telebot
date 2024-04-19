from telebot import TeleBot
from telebot.types import Message
from database import User, City
from classes import ForecastConfig

from api import forecast


TRANSLATIONS = {
    "temperature": "температуры",
    "humidity": "влажности",
    "wind_speed": "скорости ветра",
    "today": "сегодня",
    "tomorrow": "завтра",
    "next_5_days": "в ближайшие 5 дней"
}


class Forecast:
    
    def __init__(self, message: Message, bot: TeleBot) -> None:
        self.config = ForecastConfig.extract(message, bot)
        user: User = User.get(username = message.from_user.username)
        self.city: City = City.get_by_id(user.city_id)
    
    def update(self) -> None:
        raw = forecast(self.city, self.config.type, self.config.range)
        
        item_list = [*raw.items()]
        if self.config.custom:
            item_list = [item for item in item_list if self.config.min <= item[1] <= self.config.max]
        else:
            item_list.sort(key = lambda item: item[1], reverse = self.config.desc)
        self.data = item_list[: self.config.limit]
    
    def complete(self) -> str:
        acs_desc = ("Наибольшие показатели" if self.config.desc else
                    "Наименьшие показатели") if not self.config.custom else "Показатели"
        data_type, forecast_range = TRANSLATIONS[self.config.type], TRANSLATIONS[self.config.range]
        value_range = "" if not self.config.custom else " в диапазоне [{}; {}]".format(self.config.min,
                                                                                      self.config.max)
        title = f"{acs_desc} показатели {data_type} {forecast_range} в городе {self.city.name}{value_range}:"
        
        rows = [f"{datetime} : {value} {self.config.unit}" for datetime, value in self.data]
        text = "\n".join([title, *rows])
        return text
    
