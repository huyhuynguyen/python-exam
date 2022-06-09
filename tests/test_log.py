import logging
import unittest
from unittest.mock import patch

import setup_path
from modules import MyLogger
import subprocess

class TestLog(unittest.TestCase):
    def setUp(self) -> None:
        self.my_log = MyLogger()

    def test_call_filehandler_level(self):
        with patch('logging.Logger.addHandler') as mock_add_handler:
            with patch('logging.FileHandler.setLevel') as mock_setLevel:
                self.my_log.config_log_to_file('abc')
                mock_setLevel.assert_called()
                mock_setLevel.assert_called_with(logging.INFO)
            mock_add_handler.assert_called_once()
            

    @patch('modules.MyLogger.config_log_to_file')
    def test_write_log_to_file(self, config_log_file):
        with self.assertLogs() as captured:
            self.my_log.print_log_to_file(100, 'wins', 'abc')

        self.assertEqual(len(captured.records), 2)
        self.assertEqual(captured.records[0].levelno, logging.INFO)
        self.assertEqual(captured.records[1].levelno, logging.INFO)


    def test_call_streamhandler_level(self):
        with patch('logging.StreamHandler.setLevel') as mock_setLevel:
            self.my_log.config_stream_log()
            mock_setLevel.assert_called()
            mock_setLevel.assert_called_with(logging.ERROR)

    @patch('modules.MyLogger.config_stream_log')
    def test_write_log_to_stream(self, config_log_stream):
        with self.assertLogs() as captured:
            self.my_log.print_log_wrong_option_console('abc')

        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].levelno, logging.ERROR)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_log.py'], shell = True)