from database import BaseModel
from peewee import IntegerField, BlobField, TextField
import pickle


class User(BaseModel):
    id = IntegerField(primary_key = True)
    username = TextField(unique = True)
    city_id = IntegerField(null = True)
    history = BlobField(default = pickle.dumps([]))
