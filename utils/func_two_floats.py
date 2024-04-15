import re


def two_floats(string: str) -> tuple[float, float] | None:
    search_floats: list[str] = re.findall(r"\d+[.,]\d+", string)
    if len(search_floats) == 2:
        return tuple(map(lambda float_s: float(float_s.replace(",", ".")), search_floats))
    
    search_integers = re.findall(r"\d+", string)
    if len(search_integers) == 2:
        return tuple(map(float, search_integers))
    
    return None
