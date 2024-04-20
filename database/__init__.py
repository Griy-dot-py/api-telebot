from loader import db
from .model_base import BaseModel

from .model_city import City
from .model_user import User

db.create_tables([User, City])


from .func_authorize import authorize
from .func_get_user_city import get_user_city
from .func_set_user_city import set_user_city
from .func_get_city_or_create import get_city_or_create
from .func_select_cities_by_name import select_cities_by_name
