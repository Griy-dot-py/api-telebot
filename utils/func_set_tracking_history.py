from typing import Iterator, Callable
from telebot import TeleBot
from utils import track_history


def set_tracking_history(bot: TeleBot):
    msg_functions: Iterator[Callable] = map(lambda hdlr: hdlr["function"], bot.message_handlers)
    for i, func in enumerate(msg_functions):
        new_func = track_history(func)
        bot.message_handlers[i]["function"] = new_func
