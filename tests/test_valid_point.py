import unittest
from unittest.mock import patch
import subprocess
import setup_path
from modules.not_valid_point import NotValidPoint

from helpers.is_valid_point import is_valid_point

class TestValidPoint(unittest.TestCase):
    def test_valid_point_success(self):
        @is_valid_point
        def my_func(self, point = 2):
            return 2
        res = my_func(self, 2)
        self.assertEqual(res, 2)

    def test_valid_point_failed(self):
        @is_valid_point
        def my_func(self, point = '2'):
            return 1
        
        with self.assertRaises(NotValidPoint) as context:
            my_func(self, point = '2')
        self.assertEqual(str(context.exception), "Not valid point. Game's point is not number")
        

        

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_valid_point.py'], shell = True)
