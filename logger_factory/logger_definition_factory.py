from abc import ABC, abstractmethod, abstractproperty
from typing import List, NamedTuple
from collections import namedtuple

# Defaults are applied from the right
Logger = namedtuple('Logger', ['name', 'level', 'propagate', 'handlers'], defaults=[None])
Handler = namedtuple('Handler', ['name', 'level', 'formatter', 'handler_class', 'stream'], defaults=[None])
Formatter = namedtuple('Formatter', ['name', 'format'])


class LoggingDefinitionFactory:

    disable_existing_loggers = False
    version = 1

    def __init__(self, formatters: List[Formatter],  handlers: List[Handler],  loggers: List[Logger]):
        self.formatters = formatters
        self.handlers = handlers
        self.loggers = loggers

    def get_formatter_definitions(self):
        return {
            "{name}".format(name): {'format': format} for (name, format) in self.formatters
        }

    def get_handlers(self):
        return {
            "{name}".format(name): {
                'level': level,
                'formatter': formatter,
                'class': handler_class,
                'stream': stream
            } for (name, level, formatter, handler_class, stream) in self.handlers
        }

    def get_loggers(self):
        return {
            "{name}".format(name): {
                'handlers': handlers,
                'level': level,
                'propagate': propagate
            } for (name, handlers, level, propagate) in self.loggers
        }

    def __call__(self):
        return {
            'version': self.version,
            'disable_existing_loggers': self.disable_existing_loggers,
            'loggers': self.get_loggers(),
            'handlers': self.get_handlers(),
            'formatters': self.get_formatters()
        }
