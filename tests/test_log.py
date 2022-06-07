import logging
import unittest

import setup_path
from modules import MyLogger
import subprocess

class TestLog(unittest.TestCase):
    def setUp(self) -> None:
        self.my_log = MyLogger()

    def test_write_log(self):
        with self.assertLogs() as captured:
            self.my_log.print_log_to_file(100, 'wins')

        self.assertEqual(len(captured.records), 2)
        self.assertEqual(captured.records[0].levelno, logging.INFO)
        self.assertEqual(captured.records[1].levelno, logging.INFO)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_log.py'], shell = True)