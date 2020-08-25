#!/usr/bin/env python

import logging
import logging.config

# Setup logging
logging.config.dictConfig(
        {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console_formatter": {
                "format": "{asctime},{msecs:03.0f} {levelname:>9s} {module} {funcName}: {message}",
                "style": "{",
                "datefmt": "%a %H:%M:%S",
                                 }
                      },
        "handlers": {
            "root_console_handler": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "console_formatter",
                "stream": "ext://sys.stdout",
                                    },
                    },
        "root": {
            "handlers": ["root_console_handler"],
            "level": "DEBUG",
                },
        "incremental": False,
        }
    )
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.debug("Example")
