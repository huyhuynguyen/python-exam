import unittest
from unittest.mock import patch
import subprocess
import setup_path

from helpers.is_valid_point import is_valid_point

class TestValidPoint(unittest.TestCase):
    def test_valid_point_failed(self):
        with self.assertRaises(Exception) as context:
            @is_valid_point
            def a(self, point = '2'):
                return 1
            a(self, point = '2')
        self.assertIs(type(context.exception), ValueError)

    def test_valid_point_success(self):
        @is_valid_point
        def a(self, point = 2):
            return 2
        res = a(self, 2)
        self.assertEqual(res, 2)
        

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_valid_point.py'], shell = True)
