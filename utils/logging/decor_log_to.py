from typing import Callable
from functools import wraps
from loader import message_logger


def log_to(send_method: Callable) -> Callable:
    
    @wraps(send_method)
    def wrapped_method(*args, **kwargs):
        
        message_logger.debug(f"to@{args[0]}: {args[1]}")
        return send_method(*args, **kwargs)

    return wrapped_method
