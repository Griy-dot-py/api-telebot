from loader import db
from model_base import BaseModel

from model_city import City
from model_country import Country
from model_user import User


db.create_tables([User, Country, City])
