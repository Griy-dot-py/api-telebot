import requests
from config.config import API_KEY
from database import City
from utils import query

BASE_URL = "https://api.openweathermap.org/geo/1.0/direct"


def geolocation(city_name: str, all: bool = False) -> City:
    query_data = {"q": city_name, "appid": API_KEY, "limit": 4}
    url = BASE_URL + "?" + query(query_data)
    
    resp = requests.get(url).json()
    if not any(resp):
        return None
    
    if not all:
        resp = resp[0]
        try:
            city = City(name = resp["local_names"]["ru"],
                        country = resp["country"],
                        latitude = resp["lat"],
                        longitude = resp["lon"])
        except KeyError:
            city = City(name = resp["name"],
                        country = resp["country"],
                        latitude = resp["lat"],
                        longitude = resp["lon"])
        return city

    else:
        data = []
        for city in resp:
            try:
                data.append(
                    City(name = city["local_names"]["ru"],
                         country = city["country"],
                         latitude = city["lat"],
                         longitude = city["lon"])
                    )
            except KeyError:
                data.append(
                    City(name = city["name"],
                        country = city["country"],
                        latitude = city["lat"],
                        longitude = city["lon"])
                )
        return data
        
