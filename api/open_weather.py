import requests
from config.config import API_KEY
from pprint import pprint


BASE_URL = "http://api.openweathermap.org"


def geo(city_name: str,country_code: str) -> tuple[str, float, float]:
    url = f"{BASE_URL}/geo/1.0/direct?q={city_name},{country_code}&appid={API_KEY}"
    resp = requests.get(url).json()[0]
    return resp["name"], resp["lat"], resp["lon"]


def current(latitude: float, longitude: float): # °C
    url = f"{BASE_URL}/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&lang=ru&appid={API_KEY}"
    resp = requests.get(url).json()
    temp = round(resp["main"]["temp"], 1)
    feels = round(resp["main"]["feels_like"], 1)
    weather: str = resp["weather"][0]["description"]
    return f"Температура {temp}°C. {weather.capitalize()}. Ощущается как {feels}°C"
