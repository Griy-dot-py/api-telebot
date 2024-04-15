from telebot.types import Message
from loader import bot
from config.config import DEFAULT_COMMANDS, SETTING_COMMANDS, WEATHER_COMMANDS
from utils.logging import log_from


@bot.message_handler(commands = ["help"])
@log_from
def help_cmd(message: Message):
    defaults = "\n".join((
        "Что я умею делать:",
        *(f"/{cmd} - {about}" for cmd, about in DEFAULT_COMMANDS.items())
                        ))
    settings = "\n".join((
        "Настройки:",
        *(f"/{cmd} - {about}" for cmd, about in SETTING_COMMANDS.items())
    ))
    forecasts = "\n".join((
        "Прогноз погоды:",
        *(f"/{cmd} - {about}" for cmd, about in WEATHER_COMMANDS.items())
    ))
    
    text = "\n\n".join((defaults, settings, forecasts))
    bot.send_message(message.chat.id, text)
