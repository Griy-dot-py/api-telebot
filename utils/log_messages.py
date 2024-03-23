from typing import Callable
from functools import wraps
from telebot.types import Message
from telebot import TeleBot

from loader import message_logger, error_logger


def log_from(message_hdlr: Callable) -> Callable:
    
    @wraps(message_hdlr)
    def wrapped_handler(message: Message):
        incoming = f"from@{message.chat.id}: {message.text}"
        message_logger.debug(incoming)
        try:
            return  message_hdlr(message)
        except Exception as ex:
            error_logger.exception(incoming, exc_info = True)
            raise
    
    return wrapped_handler


def log_to(method: Callable) -> Callable:
    
    @wraps(method)
    def wrapped_method(*args, **kwargs):
        
        message_logger.debug(f"to@{args[0]}: {args[1]}")
        return method(*args, **kwargs)

    return wrapped_method


def set_logging_to(bot: TeleBot, log_methods: list[str]):
    for method_name in log_methods:
        old_method = getattr(bot, method_name)
        new_method = log_to(old_method)
        setattr(bot, method_name, new_method)
