from io import StringIO
import sys
from tkinter import W
import unittest
import subprocess
import setup_path
from unittest.mock import PropertyMock, patch
from modules.not_valid_choice import NotValidChoice
from helpers.is_valid_input import is_valid_input

class TestValidInput(unittest.TestCase):
    @patch('builtins.input', return_value='abcd')
    @patch('helpers.is_valid_input.re.compile')
    @patch('helpers.is_valid_input.re.fullmatch', return_value=True)
    def test_is_valid_input(self, mock_fullmatch, mock_compile, string):
        res = is_valid_input('pattern', 'label')
        self.assertEqual(res, string.return_value)

    @patch('builtins.input')
    @patch('helpers.is_valid_input.re.compile')
    @patch('helpers.is_valid_input.re.fullmatch', return_value=False)
    def test_is_valid_return_exception(self, mock_fullmatch, mock_compile, string):
        with self.assertRaises(NotValidChoice) as context:
            is_valid_input('pattern', 'label')
        self.assertEqual(str(context.exception), 'Invalid option')

    @patch('helpers.is_valid_input.re.compile')
    @patch('helpers.is_valid_input.re.fullmatch', return_value=False)
    def test_input_call_try_times(self, mock_fullmatch, mock_compile):
        with patch('builtins.input') as mock_input:
            with self.assertRaises(NotValidChoice):
                is_valid_input('pattern', 'label')
            self.assertEqual(mock_input.call_count, 3)


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_valid_input.py'], shell = True)