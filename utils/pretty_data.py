class PrettyTimeData:
    types = {"humidity" : "%",
             "temperature" : "°C",
             "wind_speed" : "m/s"}
    
    def __init__(self, type: str, raw: dict[str, float], limit: int, desc: bool = False) -> None:
        self.unit = PrettyTimeData.types[type]
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
        return "\n".join([f"{key} : {value} {self.unit}" for key, value in order])
