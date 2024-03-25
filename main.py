from loader import bot, error_logger
from telebot import custom_filters
import handlers  # noqa
import utils


if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    utils.set_default_commands(bot)
    utils.logging.set_logging_to(bot, ["send_message"])
    
    try:
        bot.infinity_polling()
    except Exception:
        error_logger.exception("", exc_info = True)
        error_logger.critical("Критческая ошибка! Работа бота остановлена")
        pass
