from typing import Callable
from telebot.types import CallbackQuery
from functools import wraps
from loader import message_logger, error_logger
from config.config import LOG_ERRORS


def log_call(callback_hdlr: Callable) -> Callable:
    
    @wraps(callback_hdlr)
    def wrapped_handler(call: CallbackQuery):
        incoming = f"call@{call.from_user.id}: {call.data}"
        message_logger.debug(incoming)
        try:
            return  callback_hdlr(call)
        except Exception:
            if LOG_ERRORS: error_logger.exception(incoming, exc_info = True)
            raise
    
    return wrapped_handler
