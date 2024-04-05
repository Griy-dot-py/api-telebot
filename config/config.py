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
    "start" : "run bot",
    "help" : "help with commands",
    "hello_world" : "print \"Hello, world!\"",
    "cancel" : "discard current operation"
}
SETTING_COMMANDS = {
    "change_city" : "change your city"
}
WEATHER_COMMANDS = {
    "current" : "check current weather in your city",
    "low": "check weather forecast and show the least weather indicators"
}
PATH_TO_DB = os.getenv("PATH_TO_DB")
LOG_ERRORS = eval(os.getenv("LOG_ERRORS").capitalize())
DEBUG_TO_FILE = eval(os.getenv("DEBUG_TO_FILE").capitalize())
