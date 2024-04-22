from telebot import TeleBot
from telebot.types import Message
from typing import Callable
from functools import wraps
from loader import message_logger


def log_reply(reply_to_method: Callable) -> Callable:
    
    @wraps(reply_to_method)
    def wrapped_method(*args, **kwargs):
        
        message_logger.debug(f"to@{args[0].from_user.id}: {args[1]}")
        return reply_to_method(*args, **kwargs)

    return wrapped_method
