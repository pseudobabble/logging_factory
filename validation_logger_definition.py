#!/usr/bin/env python3

from logger_facade import Logger, LoggingDefinitionFacade

# We want to use the same formatters and handlers as the main logger
from main_logger_definition import formatters, handlers


loggers = [
    Logger(name='', level='DEBUG', propagate=True, handlers=handlers),
    Logger(name='settings_validation', level='WARNING', propagate=True, handlers=[]),
]


ValidationLoggingDefinition = LoggingDefinitionFacade(formatters=formatters, handlers=handlers, loggers=loggers)
