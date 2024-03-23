from database.model_base import BaseModel
from peewee import IntegerField, BlobField, TextField
from loader import db


class User(BaseModel):
    id = IntegerField(primary_key = True)
    username = TextField(unique = True)
    country_id = IntegerField(null = True)
    city_id = IntegerField(null = True)
    history = BlobField(null= True)


db.create_tables([User])
