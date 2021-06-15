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


class MainLoggingDefinitionInstance(LoggingDefinitionFactory):

    disable_existing_loggers = True

    def __init__(self, formatters: List[Formatter], handlers: List[Handler], loggers: List[Logger], custom_logger_schema: 'SomeClientSchema'):
        self.custom_schema = custom_logger_schema
        super().__init__(formatters, handlers, loggers)

    # Lets say we want to handle client config...
    def get_loggers(self):
        loggers = [logger for logger in self.loggers if logger.name not in self.custom_schema.loggers]
        for logger_name, logger_configuration in self.custom_schema.loggers:
            loggers.append(
                Logger(name=logger_name, level=logger_configuration['level'], propagate=logger_configuration['propagate'])
            )
        self.loggers = loggers

        return super().get_loggers()



# Imagine we got an instance of this this from somewhere
class SomeClientSchema:
    loggers = {'documents': {'level': 'DEBUG', 'propagate': False}}
    log_to_console = False
        


MainLoggingDefinition = MainLoggingDefinitionInstance(formatters=formatters, handlers=handlers, loggers=loggers, custom_logger_schema=SomeClientSchema())
