from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter
from database import User, City
from api import geolocation


class ValidCity(AdvancedCustomFilter):
    key = "valid_city"
    
    def check(self, message: Message, param: bool):    
        if param == "soft":
            try:
                City.get(name = message.text)
            except City.DoesNotExist:
                city = geolocation(message.text)
                if city is None:
                    return False
                try:
                    City.get(name = city.name)
                except City.DoesNotExist:
                    city.save()
            return True
        
        elif param == "hard":
            try:
                City.get(name = message.text)
            except City.DoesNotExist:
                return False
            return True
        
        else:
            return True
