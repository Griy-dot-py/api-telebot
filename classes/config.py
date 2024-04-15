from telebot import TeleBot
from telebot.types import Message
from dataclasses import dataclass, field


UNITS = {"humidity" : "%",
         "temperature" : "°C",
         "wind_speed" : "м/с"}


@dataclass
class ForecastConfig:
    desc: bool
    type: str
    range: str
    limit: int
    unit: str = field(init = False)
    
    @classmethod
    def extract(cls, message: Message, bot: TeleBot) -> "ForecastConfig":
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            fc = cls(desc = data["desc"],
                     type = data["type"],
                     range = data["range"],
                     limit = int(message.text))
            
        fc.unit = UNITS[fc.type]
        return fc
