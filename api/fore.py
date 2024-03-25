from database import City
import requests, json, re
from datetime import datetime, date, timedelta
from api import API_KEY, OPEN_WEATHER_URL


def forecast(city: City, data_type: str, forecast_range: str, limit: int) -> str:
    url = OPEN_WEATHER_URL + \
        "/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}".format(lat = city.latitude,
                                                                       lon = city.longitude,
                                                                       API_key = API_KEY) + \
        "&units=metric"
    
    resp = requests.get(url).json()
    offset : int = resp["city"]["timezone"]
    for data in resp["list"]:
        data["dt"] += offset
        data["dt_txt"] = str(datetime.fromtimestamp(data["dt"]))
    
    if forecast_range == "today":
        today = str(date.today())
        print(today)
        resp["list"] = list(filter(lambda data: re.search(today, data["dt_txt"]) is not None, resp["list"]))
    if forecast_range == "tomorrow":
        tomorrow = str(date.today() + timedelta(days = 1))
        resp["list"] = list(filter(lambda data: re.search(tomorrow, data["dt_txt"]) is not None, resp["list"]))
        
    # with open("test.json", "w") as file:
    #     json.dump(resp, file, indent = 4)
