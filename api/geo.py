import requests
from config.config import API_KEY
from utils import query

BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"


def geolocation(city_name: str,country_code: str) -> tuple[str, float, float]:
    query_data = {"q" : (city_name, country_code),
                  "appid" : API_KEY}
    url = BASE_URL + "?" + query(query_data)
    
    resp = requests.get(url).json()[0]
    return resp["name"], resp["lat"], resp["lon"]
