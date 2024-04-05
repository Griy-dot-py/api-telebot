from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter
from database import Country
from api import search_by_name


class ValidCountry(AdvancedCustomFilter):
    key = "valid_country"
    
    def check(self, message: Message, text: str):
        if text == "soft":
            try:
                Country.get(name = message.text)
            except Country.DoesNotExist:  
                try_to_search = search_by_name(message.text)
                if try_to_search is None:
                    return False
                code, common = try_to_search
                try:
                    Country.get(code = code)
                except Country.DoesNotExist:
                    country = Country(name = common, code = code)
                    country.save()
            return True
        
        elif text == "hard":
            try:
                Country.get(name = message.text)
            except Country.DoesNotExist:
                return False
            return True

        
        else:
            return True
