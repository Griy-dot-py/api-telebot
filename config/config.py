import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Cannot load environment variables. There's no .env file")
else:
    load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
COMMANDS = {
    "start" : "Run bot",
    "hello_world" : "print \"Hello, world!\"",
    "change_city" : "change city",
    "current" : "current weather in your city",
    "low": "the least value",
    # "help" : "Print instructions"
}
PATH_TO_DB = os.getenv("PATH_TO_DB")
LOG_ERRORS = eval(os.getenv("LOG_ERRORS").capitalize())
DEBUG_TO_FILE = eval(os.getenv("DEBUG_TO_FILE").capitalize())
