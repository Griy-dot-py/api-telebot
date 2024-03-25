import requests
from api import OPEN_WEATHER_URL, API_KEY


def current_weather(latitude: float, longitude: float): # °C
    url = f"{OPEN_WEATHER_URL}/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&lang=ru&appid={API_KEY}"
    resp = requests.get(url).json()
    temp = round(resp["main"]["temp"], 1)
    feels = round(resp["main"]["feels_like"], 1)
    weather: str = resp["weather"][0]["description"]
    return f"Температура {temp}°C. {weather.capitalize()}. Ощущается как {feels}°C"
