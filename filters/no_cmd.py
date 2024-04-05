from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter


class NoCommand(AdvancedCustomFilter):
    key = "no_cmd"
    
    def check(self, message: Message, text: bool):
        if text is True:
            return not message.text.startswith("/")
        return True