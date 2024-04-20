from database import City


def get_city_or_create(name: str, country: str, latitude: str, longitude: str) -> City:
    city, *_ = City.get_or_create(name = name, country = country, latitude = latitude, longitude = longitude)
    return city
