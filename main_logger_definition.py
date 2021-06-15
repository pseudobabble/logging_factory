#!/usr/bin/env python3
from logging.handlers import RotatingFileHandler

from logger_factory import Logger, Handler, Formatter, LoggingDefinitionFactory


formatters = [
    Formatter(name='standard', format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'),
    Formatter(name='big-wow', format='WOW LOOK AT THE %(asctime)s, I NEED TO GO UP TO LEVEL [%(levelname)s] TO DELIVER THIS MESSAGE ADDRESSED TO OUR SYSADMIN MR %(name)s: %(message)s'),
]

handlers = [
    Handler(name='stdout_handler', level='DEBUG', formatter='standard', formatter_class='logging.StreamHandler', stream='ext://sys.stdout'),
    Handler(name='kaboom', level='CRITICAL', formatter='big-wow', formatter_class=RotatingFileHandler('/some/path/'))

]

loggers = [
    Logger(name='', level='DEBUG', propagate=True, handlers=handlers),
    Logger(name='documents', level='INFO', propagate=True),
    Logger(name='analysis', level='WARNING', propagate=True),
]

class MainLoggingDefinition(LoggingDefinitionFactory):

    disable_existing_loggers = True

    def get_handlers(self, use_stdout: bool = False):
        handlers = super().get_handlers()
        del handlers['kaboom']

        return handlers
