import requests

BASE_URL = "https://restcountries.com/v3.1"


def search_by_name(country_name: str) -> tuple[str, str]: # -> country_code, common_name
    try:
        resp = requests.get(f"{BASE_URL}/name/{country_name}").json()[0]
        name = resp["name"]["common"]
        code = resp["cca2"]
        return name, code
    except KeyError:
        return None
