from typing import OrderedDict
import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Cannot load environment variables. There's no .env file")
else:
    load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
DEFAULT_COMMANDS = {
    "start" : "запустить бота",
    "help" : "список комманд",
    "hello_world" : "написать \"Привет, мир!\"",
    "cancel" : "отменить текущую операцию"
}
SETTING_COMMANDS = {
    "change_city" : "сменить город"
}
WEATHER_COMMANDS = {
    "current" : "погода в вашем городе сейчас",
    "low": "наименьшие значения показателей прогноза погоды",
    "high": "наибольшие значения показателей прогноза погоды",
}
PATH_TO_DB = os.getenv("PATH_TO_DB")
LOG_ERRORS = eval(os.getenv("LOG_ERRORS").capitalize())
DEBUG_TO_FILE = eval(os.getenv("DEBUG_TO_FILE").capitalize())
