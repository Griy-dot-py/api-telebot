from database import City


def get_city_by_id(id: int) -> City:
    city = City.get_or_none(id = id)
    return city
