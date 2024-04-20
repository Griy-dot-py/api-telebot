from telebot import TeleBot
from telebot.types import Message
from typing import Callable
from functools import wraps
from loader import message_logger


def log_reply(reply_to_method: Callable) -> Callable:
    
    @wraps(reply_to_method)
    def wrapped_method(self: TeleBot, message: Message, text: str, **kwargs):
        
        message_logger.debug(f"to@{message.from_user.id}: {text}")
        return reply_to_method(self, message, text, **kwargs)

    return wrapped_method
