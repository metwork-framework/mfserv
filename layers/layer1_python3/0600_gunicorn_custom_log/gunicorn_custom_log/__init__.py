import logging
from gunicorn.glogging import Logger, CONFIG_DEFAULTS
from logging.config import dictConfig

# dummy wrapper to fix https://github.com/metwork-framework/mfserv/issues/47


class StdoutFilter(logging.Filter):
    """Filter class which keeps log records for stdout (ie. < WARNING)."""

    def filter(self, record):
        return record.levelno < logging.WARNING


class StderrFilter(logging.Filter):
    """Filter class which keep log records for stderr (ie. >= WARNING)."""

    def filter(self, record):
        return record.levelno >= logging.WARNING


class CustomLogger(Logger):

    def setup(self, cfg):
        Logger.setup(self, cfg)
        CONFIG_DEFAULTS['handlers']['console']['filters'] = \
            ["stdout_filter"]
        CONFIG_DEFAULTS['handlers']['error_console']['filters'] = \
            ["stderr_filter"]
        CONFIG_DEFAULTS['loggers']['gunicorn.error']['handlers'] = \
            ['console', 'error_console']
        CONFIG_DEFAULTS['filters'] = {
            "stdout_filter": {
                "()": "gunicorn_custom_log.StdoutFilter"
            },
            "stderr_filter": {
                "()": "gunicorn_custom_log.StderrFilter"
            }
        }
        CONFIG_DEFAULTS['disable_existing_loggers'] = True
        dictConfig(CONFIG_DEFAULTS)
