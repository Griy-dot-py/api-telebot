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
    custom: bool
    min: float = field(default = None, init = False)
    max: float = field(default = None, init = False)
    unit: str = field(init = False)
    
    @classmethod
    def extract(cls, message: Message, bot: TeleBot) -> "ForecastConfig":
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            if data["custom"] and type(data) is dict:
                custom_values = data.pop("custom_values")
            fc = cls(**data, limit = int(message.text))
        
        if fc.custom:
            fc.min, fc.max = sorted(custom_values)
        fc.unit = UNITS[fc.type]
        return fc
