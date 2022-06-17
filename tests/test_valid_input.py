from io import StringIO
import sys
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
    def test_is_valid_input(self, fullmatch_mock, compile_mock, string):
        res = is_valid_input('pattern', 'label')
        self.assertEqual(res, string.return_value)

    @patch('builtins.input')
    @patch('helpers.is_valid_input.re.compile')
    @patch('helpers.is_valid_input.re.fullmatch', return_value=False)
    def test_is_valid_return_exception(self, fullmatch_mock, compile_mock, string):
        # captured_output = StringIO()
        # sys.stdout = captured_output
        with self.assertRaises(NotValidChoice) as context:
            is_valid_input('pattern', 'label')
            self.assertIs(type(context.exception), NotValidChoice)
        # self.assertIn("Invalid option\n", captured_output.getvalue())
        # self.assertIs(res, NotValidChoice)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_valid_input.py'], shell = True)