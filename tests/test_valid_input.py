from io import StringIO
import sys
import unittest
import subprocess
from unittest.mock import PropertyMock, patch
import setup_path
from helpers.is_valid_input import is_valid_input

class TestValidInput(unittest.TestCase):
    @patch('builtins.input', return_value='abcd')
    @patch('helpers.is_valid_input.re.compile')
    @patch('helpers.is_valid_input.re.fullmatch', return_value=True)
    def test_is_valid_input(self, fullmatch_mock, compile_mock, string):
        res = is_valid_input('abc', 'abc')
        self.assertEqual(res, string.return_value)

    @patch('builtins.input')
    @patch('helpers.is_valid_input.re.compile')
    @patch('helpers.is_valid_input.re.fullmatch', return_value=False)
    def test_is_valid_return_exception(self, fullmatch_mock, compile_mock, string):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        res = is_valid_input('abc', 'abc')
        self.assertIn("Invalid option\n", capturedOutput.getvalue())
        self.assertIs(res, ValueError)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_valid_input.py'], shell = True)