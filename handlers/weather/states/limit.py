from telebot.types import Message
from loader import bot
from states import AskFor
from database import User, City
from utils import PrettyTimeData
from utils.logging import log_from
from api import forecast


@bot.message_handler(state = AskFor.limit)
@log_from
def take_limit(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        desc = data["desc"]
        dtype = data["type"]
        frange = data["range"]
        limit = int(message.text)
    
    user: User = User.get(username = message.from_user.username)
    city: City = City.get_by_id(user.city_id)
    forecast_values = forecast(city, dtype, frange)
    
    pretty_values = PrettyTimeData(raw = forecast_values,
                                   limit = limit,
                                   desc = desc)
    n_est, the = "highest" if desc else "least", "the " if len(forecast_values) > 8 else ""
    title = f"The {n_est} values of {dtype} for {the}{frange} in {city.name}:"
    text = "\n".join((title, *repr(pretty_values).split("\n")))
    
    bot.send_message(message.chat.id, text)
    bot.delete_state(message.from_user.id, message.chat.id)
