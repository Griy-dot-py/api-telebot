import requests
from config.config import API_KEY
from database import City
from utils import query

BASE_URL= "http://api.openweathermap.org/data/2.5/weather"


def current_weather(city: City): # °C
    query_data = {"lat": city.latitude,
                  "lon" : city.longitude,
                  "units" : "metric",
                  "lang" : "ru",
                  "appid" : API_KEY}
    url = BASE_URL + "?" + query(query_data)
    
    resp = requests.get(url).json()
    temp = round(resp["main"]["temp"], 1)
    feels = round(resp["main"]["feels_like"], 1)
    weather: str = resp["weather"][0]["description"]
    return f"Температура {temp}°C. {weather.capitalize()}. Ощущается как {feels}°C"
