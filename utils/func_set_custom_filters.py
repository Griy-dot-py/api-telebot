from telebot import TeleBot

def set_custom_filters(bot: TeleBot, *args) -> None:
    for f in args:
        bot.add_custom_filter(f)
