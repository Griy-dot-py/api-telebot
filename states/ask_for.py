from telebot.handler_backends import StatesGroup, State


class AskFor(StatesGroup):
    city = State()
    dtype = State()
    frange = State()
    limit = State()
