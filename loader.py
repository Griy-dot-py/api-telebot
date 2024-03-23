from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from peewee import SqliteDatabase
import json, logging.config
from config import config


with open("logging/logging_config.json") as json_conf:
    dict_conf = json.load(json_conf)
logging.config.dictConfig(dict_conf)
storage = StateMemoryStorage()


bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
db = SqliteDatabase(config.PATH_TO_DB)
message_logger = logging.getLogger("messages")
error_logger = logging.getLogger("errors")
