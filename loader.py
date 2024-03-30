from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from peewee import SqliteDatabase
import logging.config, os
from config import config, dict_config


try:
    logging.config.dictConfig(dict_config)
except ValueError:
    os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs"))
    logging.config.dictConfig(dict_config)
debug_logger_name = "messages.file_debug" if config.DEBUG_TO_FILE else "messages"
storage = StateMemoryStorage()


bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
db = SqliteDatabase(config.PATH_TO_DB)
message_logger = logging.getLogger(debug_logger_name)
error_logger = logging.getLogger("errors")
