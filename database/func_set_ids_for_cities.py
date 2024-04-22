from database import City


def set_ids_for_cities(cities: list[City]) -> list[City]:
    cities_with_ids = []
    for city in cities:
        db_city: City = City.get_or_none(name = city.name, country = city.country)
        if db_city is None:
            city.save()
            cities_with_ids.append(city)
        else:
            cities_with_ids.append(db_city)
    return cities_with_ids
