#!/usr/bin/env python3

from logger_factory import Logger, LoggingDefinitionFactory

# We want to use the same formatters and handlers as the main logger
from main_logger import formatters, handlers


loggers = [
    Logger(name='', level='DEBUG', propagate=True, handlers=handlers),
    Logger(name='settings_validation', level='WARNING', propagate=True),
]


ValidationLoggingDefinition = LoggingDefinitionFactory(formatters=formatters, handlers=handlers, loggers=loggers)
