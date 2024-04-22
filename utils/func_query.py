from typing import Any

def query(data: dict[str, Any]):
    for key, value in data.items():
        if type(value) in (list, tuple):
            data[key] = ",".join(map(str, value))
        else:
            data[key] = str(value)
    return "&".join(f"{key}={value}" for key, value in data.items())
