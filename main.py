from loader import bot, error_logger
from telebot.custom_filters import StateFilter
from filters import NoCommand, ValidCity, ValidLimit, ValidValues
import handlers  # noqa
import utils


if __name__ == "__main__":
    utils.set_custom_filters(bot,
                             StateFilter(bot),
                             ValidCity(),
                             NoCommand(),
                             ValidLimit(),
                             ValidValues())
    utils.set_all_commands(bot)
    utils.logging.set_logging_to(bot, ["send_message"])
    
    try:
        bot.infinity_polling()
    except Exception:
        error_logger.exception("", exc_info = True)
        error_logger.critical("Критческая ошибка! Работа бота остановлена")
        pass
