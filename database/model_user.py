from database import BaseModel
from peewee import IntegerField, BlobField, TextField


class User(BaseModel):
    id = IntegerField(primary_key = True)
    username = TextField(unique = True)
    country_id = IntegerField(null = True)
    city_id = IntegerField(null = True)
    history = BlobField(null= True)
