LOGGING_CFG = {
    "version": 1,
    "root": {
        "level": "INFO",
        "handlers": ["console", ]
    },
    "formatters": {
        "standard": {
            "format": "%(asctime)s -- %(filename)s -- %(levelname)s -- %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        }
    }
}

