from telebot import TeleBot
from utils.logging import log_to


def set_logging_to(bot: TeleBot, sending_methods: list[str]):
    for method_name in sending_methods:
        old_method = getattr(bot, method_name)
        new_method = log_to(old_method)
        setattr(bot, method_name, new_method)
