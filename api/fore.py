from database import City
import requests, re
from time import time
import datetime as dt
from config.config import API_KEY
from utils import query


BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


def forecast(city: City, data_type: str, forecast_range: str) -> dict:
    query_data = {"lat" : city.latitude,
                  "lon": city.longitude,
                  "appid": API_KEY,
                  "units" : "metric"}
    url = BASE_URL + "?" + query(query_data)
    resp = requests.get(url).json()
    
    #Convert to user's timezone
    offset : int = resp["city"]["timezone"]
    main_list = resp["list"]
    for data in main_list:
        data["dt"] += offset
        data["dt_txt"] = str(dt.datetime.fromtimestamp(data["dt"]))
    
    #Take only data we need
    if data_type == "temperature":
        values = {data["dt_txt"][: -3]: data["main"]["temp"] for data in main_list}
    elif data_type == "humidity":
        values = {data["dt_txt"][: -3]: data["main"]["humidity"] for data in main_list}
    elif data_type == "wind_speed":
        values = {data["dt_txt"][: -3]: round(data["wind"]["speed"], 1) for data in main_list}
    else:
        raise ValueError(f"Invalid data type '{data_type}'")
    values: dict[str, float]
    
    #Filer data with user's forecast range
    if forecast_range in ("today", "tomorrow"):
        now = dt.datetime.fromtimestamp(int(time()) + offset)
        date = str(now).split(" ")[0]
        if forecast_range == "today":
            date = str(now).split(" ")[0]
        else:
            date = str(now + dt.timedelta(days = 1)).split(" ")[0]       
        values = {":".join(key.split(" ")[1].split(':')) : value for key, value in values.items()
                  if re.search(date, key) is not None}
    
    return values
