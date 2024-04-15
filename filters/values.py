from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter
from utils import two_floats


class ValidValues(AdvancedCustomFilter):
    key = "valid_values"
    
    def check(self, message: Message, param: bool):
        floats = two_floats(message.text)
        if param is True and floats is not None:
            return True
        
        elif param is True and floats is None:
            return False
        
        else:
            return True
