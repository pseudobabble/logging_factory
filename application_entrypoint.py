#!/usr/bin/env python3

import logging

from main_logger_definition import MainLoggingDefinition
from validation_logger_definition import ValidationLoggingDefinition


def set_up_logging():
    if validate_settings:
        logging.config.dictConfig(ValidationLoggingDefinition())
    else:
        logging.config.dictConfig(MainLoggingDefinition())
