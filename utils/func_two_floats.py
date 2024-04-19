import re


def two_floats(string: str) -> tuple[float, float] | None:
    search_floats = [flt.replace(",", ".") for flt in re.findall(r"\d+[.,]\d+", string)]
    search_integers = re.findall(r"\d+", string)
    
    if len(search_floats) == 2:
        return tuple(map(float, search_floats))
    elif len(search_integers) == 2:
        return tuple(map(float, search_integers))
    elif len(search_integers) == 3:
        for fake_int in search_floats[0].split("."):
            search_integers.remove(fake_int)
        return (float(*search_integers), float(*search_floats))
    return None
