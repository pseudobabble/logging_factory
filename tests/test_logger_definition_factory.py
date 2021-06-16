
import unittest

from logger_facade import LoggingDefinitionFacade, Formatter, Handler, Logger

class TestLoggerDefinitionFactory(unittest.TestCase):

    def test_get_formatter_definitions(self):
        formatter = Formatter(name='test-formatter', format='[%(levelname)s] %(name)s: %(message)s')
        handler = Handler(name='test-handler', level='DEBUG', formatter='test_formatter', handler_class='logging.StreamHandler', stream='ext://sys.stdout')
        logger = Logger(name='test-logger', level='DEBUG', propagate=True, handlers=[handler])

        TestLoggingDefinition = LoggingDefinitionFacade(formatters=[formatter], handlers=[handler], loggers=[logger])

        self.assertEqual(
            TestLoggingDefinition.get_formatter_definitions(),
            {"test-formatter": {'format': '[%(levelname)s] %(name)s: %(message)s'}}

        )

    def test_get_handler_definitions(self):
        formatter = Formatter(name='test-formatter', format='[%(levelname)s] %(name)s: %(message)s')
        handler = Handler(name='test-handler', level='DEBUG', formatter='test_formatter', handler_class='logging.StreamHandler', stream='ext://sys.stdout')
        logger = Logger(name='test-logger', level='DEBUG', propagate=True, handlers=[handler])

        TestLoggingDefinition = LoggingDefinitionFacade(formatters=[formatter], handlers=[handler], loggers=[logger])

        self.assertEqual(
            TestLoggingDefinition.get_handler_definitions(),
            {
                "test-handler": {
                    'level': 'DEBUG',
                    'formatter': 'test_formatter',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout'
                }
            }
        )

    def test_get_logger_definitions(self):
        formatter = Formatter(name='test-formatter', format='[%(levelname)s] %(name)s: %(message)s')
        handler = Handler(name='test-handler', level='DEBUG', formatter='test_formatter', handler_class='logging.StreamHandler', stream='ext://sys.stdout')
        logger = Logger(name='test-logger', level='DEBUG', propagate=True, handlers=[handler])

        TestLoggingDefinition = LoggingDefinitionFacade(formatters=[formatter], handlers=[handler], loggers=[logger])

        self.assertEqual(
            TestLoggingDefinition.get_logger_definitions(),
            {
                "test-logger": {
                    'handlers': ['test-handler'],
                    'level': 'DEBUG',
                    'propagate': True
                }
            }
        )


if __name__ == '__main__':
    unittest.main()
