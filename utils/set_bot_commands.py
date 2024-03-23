from telebot.types import BotCommand
from telebot import TeleBot
from config.config import COMMANDS


def set_default_commands(bot: TeleBot):
    bot.set_my_commands(
        [BotCommand(*i) for i in COMMANDS.items()]
    )
