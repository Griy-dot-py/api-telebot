from telebot.types import BotCommand
from telebot import TeleBot
from config.config import DEFAULT_COMMANDS, SETTING_COMMANDS, WEATHER_COMMANDS


def set_all_commands(bot: TeleBot):
    cmds = DEFAULT_COMMANDS.copy()
    cmds.update(SETTING_COMMANDS)
    cmds.update(WEATHER_COMMANDS)
    bot.set_my_commands(
        [BotCommand(*i) for i in cmds.items()]
    )
