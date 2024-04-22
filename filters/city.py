from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter
from database import select_cities_by_name, set_ids_for_cities
from api import geolocation


class ValidCity(AdvancedCustomFilter):
    key = "valid_city"
    
    def check(self, message: Message, param: bool):   
        if param == "soft":
            cities = geolocation(message.text)
            if cities is None:
                return False
            set_ids_for_cities(cities)
            return True
        
        elif param == "hard":
            cities = select_cities_by_name(message.text)
            if cities is None or len(cities) > 1:
                return False
            return True
        
        else:
            return True
