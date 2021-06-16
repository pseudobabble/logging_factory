#!/usr/bin/env python3

import sys
from pprint import pprint

from main_logger_definition import MainLoggingDefinition
from validation_logger_definition import ValidationLoggingDefinition



def set_up_logging():
    validation_logging_definition = ValidationLoggingDefinition()
    pprint(validation_logging_definition)
    print('\n\n\n\n\n')

    main_logging_definition = MainLoggingDefinition()
    pprint(main_logging_definition)



if __name__ == '__main__':
    set_up_logging()
