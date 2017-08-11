import logging
import os
import sys
import unittest

from impulsare_logger import Logger

base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, base_dir + '/../')


# https://docs.python.org/3/library/unittest.html#assert-methods
class TestLogger(unittest.TestCase):
    def test_config_not_exists(self):
        with self.assertRaisesRegex(IOError, 'Missing config file: ".+" does not exist'):
            Logger('pytest', '/does/not/exist')


    def test_log_not_writeable(self):
        with self.assertRaisesRegex(IOError, "Can't write to '.+writeable.+pytest\.log'"):
            Logger('pytest', base_dir + '/static/config_notwriteable.yml')


    def test_log_config_invalid(self):
        with self.assertRaisesRegex(ValueError, "Your config is not valid: True is not of type 'string'"):
            Logger('pytest', base_dir + '/static/config_invalid.yml')


    def test_log_config_valid(self):
        if os.path.isfile('/tmp/test.log'):
            os.remove('/tmp/test.log')

        logger = Logger('pytest', base_dir + '/static/config_valid.yml')

        logger.log.warning('Hello')
        fileobj = open(logger.filename, 'r')
        self.assertRegex(fileobj.readline(), '.+ :: WARNING :: Hello')

        # Not working, see later
        # out, err = capsys.readouterr()
        # self.assertEqual('Hello', out)

        os.remove(logger.filename)

        logger.log.debug('Not here')
        self.assertFalse(os.path.isfile(logger.filename))

        # clean handlers
        logging.getLogger('pytest').handlers = []


    def test_log_config_valid_nologger(self):
        if os.path.isfile('/tmp/test.log'):
            os.remove('/tmp/test.log')

        logger = Logger('pytest', base_dir + '/static/config_valid_nolog.yml')

        logger.log.warning('Hello')
        self.assertFalse(os.path.isfile('/tmp/test.log'))


if __name__ == "__main__":
    unittest.main()
