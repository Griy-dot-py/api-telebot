from loader import bot, error_logger
from telebot.custom_filters import StateFilter
import filters
import handlers  # noqa
import utils


if __name__ == "__main__":
    utils.set_custom_filters(bot,
                             StateFilter(bot),
                             filters.ValidCity(),
                             filters.NoCommand(),
                             filters.ValidLimit(),
                             filters.ValidValues())
    utils.set_all_commands(bot)
    utils.logging.set_logging_to(bot, ["send_message"])
    utils.logging.set_logging_from(bot)
    utils.logging.set_logging_reply(bot)
    
    try:
        bot.infinity_polling()
    except Exception:
        error_logger.exception("", exc_info = True)
        error_logger.critical("Критческая ошибка! Работа бота остановлена")
        pass
