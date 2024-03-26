from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter
from database import User, Country, City
from api import geolocation


class ValidCity(AdvancedCustomFilter):
    key = "valid_city"
    
    def check(self, message: Message, text: bool):
        if text == "soft":
            try:
                City.get(name = message.text)
            except City.DoesNotExist:
                user: User = User.get(username = message.from_user.username)
                country: Country = Country.get_by_id(user.country_id)
                try_to_search = geolocation(message.text, country.code)
                if try_to_search is None:
                    return False
                common, lat, lon = try_to_search
                try:
                    City.get(name = common)
                except City.DoesNotExist:
                    city = City(name = common, country_id = country.id, latitude = lat, longitude = lon)
                    city.save()
            return True
        
        elif text == "hard":
            try:
                City.get(name = message.text)
            except City.DoesNotExist:
                return False
            return True
        
        else:
            return True
