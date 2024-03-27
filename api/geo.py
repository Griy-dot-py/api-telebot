import requests
from config.config import API_KEY
from utils import query

BASE_URL = "https://api.openweathermap.org/geo/1.0/direct"


def geolocation(city_name: str, country_code: str, all: bool = False
                ) -> tuple[str, float, float] | list[tuple[str, float, float]]:
    query_data = {"q" : (city_name, country_code), "appid" : API_KEY}
    url = BASE_URL + "?" + query(query_data)
    
    resp = requests.get(url).json()
    try:
        resp[0]
        if not all:
            resp = resp[0]
            return resp["name"], resp["lat"], resp["lon"]
        else:
            data = [(city["name"], city["lat"], city["lon"]) for city in resp]
            return data
    except IndexError:
        return None
