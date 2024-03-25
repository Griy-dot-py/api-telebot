from telebot.handler_backends import StatesGroup, State


class AskFor(StatesGroup):
    country = State()
    city = State()
    dtype = State()
    frange = State()
    limit = State()
