from database import BaseModel
from peewee import IntegerField, TextField, FloatField


class City(BaseModel):
    id = IntegerField(primary_key = True)
    name = TextField()
    country = TextField()
    latitude = FloatField()
    longitude = FloatField()
