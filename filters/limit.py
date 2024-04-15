from loader import bot
from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter
from database import City, User
from api import forecast


class ValidLimit(AdvancedCustomFilter):
    key = "valid_limit"
    
    def check(self, message: Message, param: bool):
        if param is True:
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                dtype = data["type"]
                frange = data["range"]
                try:
                    limit = int(message.text)
                except ValueError:
                    bot.reply_to(message, "Только одно целое число!")
                    return False
            
            user: User = User.get(username = message.from_user.username)
            city: City = City.get_by_id(user.city_id)

            forecast_values = forecast(city, dtype, frange)
            stamps_left = len(forecast_values)

            if limit < 1:
                bot.reply_to(message, "Слишком маленькое число!")
                is_filtered = False
            elif frange == "today" and stamps_left < limit:
                bot.reply_to(message, f"Не чаще 1 измерения в 3 часа! Значений осталось на сегодня: {stamps_left}")
                is_filtered = False
            elif (frange == "tomorrow" and limit > 8) or (frange == "next_5_days" and limit > 40):
                bot.reply_to(message, f"Не чаще 1 измерения в 3 часа!")
                is_filtered = False
                
            else:
                is_filtered = True
            
            return is_filtered
        
        else:
            return True
