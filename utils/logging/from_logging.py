from typing import Callable
from telebot.types import Message
from functools import wraps
from loader import message_logger, error_logger
from config.config import LOG_ERRORS


def log_from(message_hdlr: Callable) -> Callable:
    
    @wraps(message_hdlr)
    def wrapped_handler(message: Message):
        incoming = f"from@{message.chat.id}: {message.text}"
        message_logger.debug(incoming)
        try:
            return  message_hdlr(message)
        except Exception:
            if LOG_ERRORS: error_logger.exception(incoming, exc_info = True)
            raise
    
    return wrapped_handler
