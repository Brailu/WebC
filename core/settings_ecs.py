import os
...
# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/#configuring-logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("DJANGO_DEBUG_LEVEL", "INFO"),
    }
}
