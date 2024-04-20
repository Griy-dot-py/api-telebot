from database import City


def select_cities_by_name(name: str) -> list[City]:
    city_list = [*City.select().where(City.name == name)]
    return city_list
