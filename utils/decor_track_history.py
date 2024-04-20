from typing import Callable
from telebot.types import Message
from functools import wraps
from database import update_history



def track_history(message_hdlr: Callable) -> Callable:
    
    @wraps(message_hdlr)
    def wrapped_handler(message: Message):
        update_history(message)
        return  message_hdlr(message)
    
    return wrapped_handler
