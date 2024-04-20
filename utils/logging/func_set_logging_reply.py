from telebot import TeleBot
from utils.logging import log_reply


def set_logging_reply(bot: TeleBot):
    old_method = getattr(bot, "reply_to")
    new_method = log_reply(old_method)
    setattr(bot, "reply_to", new_method)
