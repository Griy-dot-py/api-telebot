from typing import Iterator, Callable
from telebot import TeleBot
from utils.logging import log_call, log_from


def set_logging_from(bot: TeleBot):
    msg_functions: Iterator[Callable] = map(lambda hdlr: hdlr["function"], bot.message_handlers)
    for i, func in enumerate(msg_functions):
        new_func = log_from(func)
        bot.message_handlers[i]["function"] = new_func
        
    cbq_functions: Iterator[Callable] = map(lambda hdlr: hdlr["function"], bot.callback_query_handlers)
    for i, func in enumerate(cbq_functions):
        new_func = log_call(func)
        bot.callback_query_handlers[i]["function"] = new_func
