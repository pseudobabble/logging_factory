from typing import List, Optional
from collections import namedtuple

# Defaults are applied from the right
Logger = namedtuple('Logger', ['name', 'level', 'propagate', 'handlers'], defaults=[None])
Handler = namedtuple('Handler', ['name', 'level', 'formatter', 'handler_class', 'stream'], defaults=[None])
Formatter = namedtuple('Formatter', ['name', 'format'])


class ConfigurationNotFound(Exception):
    pass


class LoggingDefinitionFactory:

    disable_existing_loggers = False
    version = 1

    def __init__(
            self,
            formatters: Optional[List[Formatter]] = None,
            handlers: Optional[List[Handler]] = None,
            loggers: Optional[List[Logger]] = None
    ):
        self.formatters = formatters
        self.handlers = handlers
        self.loggers = loggers

    def get_formatter_definitions(self):
        if not self.formatters:
            raise ConfigurationNotFound(
                'A list of Formatters must be provided on instantiation to request the formatter definitions'
        )

        return {
            "{}".format(name): {'format': format} for (name, format) in self.formatters
        }

    def get_handler_definitions(self):
        if not self.handlers:
            raise ConfigurationNotFound(
                'A list of Handlers must be provided on instantiation to request the handler definitions'
        )

        return {
            "{}".format(name): {
                'level': level,
                'formatter': formatter,
                'class': handler_class,
                'stream': stream
            } for (name, level, formatter, handler_class, stream) in self.handlers
        }

    def get_logger_definitions(self):
        if not self.loggers:
            raise ConfigurationNotFound(
                'A list of Loggers must be provided on instantiation to request the logger definitions'
        )

        return {
            "{}".format(name): {
                'handlers': [handler.name for handler in handlers],
                'level': level,
                'propagate': propagate
            } for (name, level, propagate, handlers) in self.loggers
        }

    def __call__(self):
        return {
            'version': self.version,
            'disable_existing_loggers': self.disable_existing_loggers,
            'loggers': self.get_logger_definitions(),
            'handlers': self.get_handler_definitions(),
            'formatters': self.get_formatter_definitions()
        }
