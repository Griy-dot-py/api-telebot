from typing import OrderedDict
from pprint import pprint

class PrettyTimeData:
    
    def __init__(self, raw: dict[str, float | int], limit: int, desc: bool = False) -> None:
        self.raw = raw
        self.limit = limit
        self.desc = desc
    
    def __sort(self):
        order = [*self.raw.items()]
        order.sort(key = lambda item: item[1], reverse = self.desc)
        order = order[: self.limit]
        return order
    
    def all(self):
        return self.__sort()
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        order = self.__sort()
        return "\n".join([f"{key} : {value}" for key, value in order])
