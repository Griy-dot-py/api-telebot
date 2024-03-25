from typing import Callable
from functools import wraps
from loader import message_logger


def log_to(method: Callable) -> Callable:
    
    @wraps(method)
    def wrapped_method(*args, **kwargs):
        
        message_logger.debug(f"to@{args[0]}: {args[1]}")
        return method(*args, **kwargs)

    return wrapped_method
