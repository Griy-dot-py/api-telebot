import os

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s(%(levelname)s) : %(asctime)s : %(message)s"
        }
    },
    "handlers": {
        "terminal": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "error_file": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "base",
            "filename": os.path.join('logs', 'errors.log'),
            "mode": "a"
        },
        "debug_file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": os.path.join('logs', 'debug.log'),
            "mode": "a"
        }
    },
    "loggers": {
        "messages": {
            "level": "DEBUG",
            "handlers": ["terminal"]
        },
        "errors": {
            "level": "ERROR",
            "handlers": ["terminal", "error_file"]
        },
        "messages.file_debug": {
            "level": "DEBUG",
            "handlers": ["debug_file"]
        }
    }
}
