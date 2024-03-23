from database.model_base import BaseModel
from peewee import IntegerField, TextField, FloatField, FixedCharField
from loader import db


class City(BaseModel):
    id = IntegerField(primary_key = True)
    name = TextField()
    country_id = IntegerField()
    latitude = FloatField()
    longitude = FloatField()


class Country(BaseModel):
    id = IntegerField(primary_key = True)
    name = TextField()
    code = FixedCharField(max_length = 2)


db.create_tables([City, Country])
