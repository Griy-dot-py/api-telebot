from database import BaseModel
from peewee import IntegerField, TextField, FixedCharField


class Country(BaseModel):
    id = IntegerField(primary_key = True)
    name = TextField()
    code = FixedCharField(max_length = 2)
