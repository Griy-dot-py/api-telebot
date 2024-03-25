import requests
from api import OPEN_WEATHER_URL, API_KEY


def geolocation(city_name: str,country_code: str) -> tuple[str, float, float]:
    url = f"{OPEN_WEATHER_URL}/geo/1.0/direct?q={city_name},{country_code}&appid={API_KEY}"
    resp = requests.get(url).json()[0]
    return resp["name"], resp["lat"], resp["lon"]
