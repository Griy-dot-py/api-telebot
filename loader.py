from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from peewee import SqliteDatabase
from config import config


storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
db = SqliteDatabase(config.PATH_TO_DB)
