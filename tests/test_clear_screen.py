import setup_path
import unittest
from unittest.mock import PropertyMock, patch
from helpers.clear_screen import clear_screen as clscreen
import subprocess

class TestClearScreen(unittest.TestCase):
    def test_is_clear_screen_called(self):
        with patch('helpers.clear_screen.subprocess.run') as mock_object:
            clscreen()
            mock_object.assert_called()
            mock_object.assert_called_with(['cls'], check=True, shell=True)

    @patch('helpers.clear_screen.enums.CLS_COMMAND_WINDOWS', new_callable = PropertyMock, return_value = ['clssss'])
    def test_is_clear_screen_failed(self, command_clear):
        with self.assertRaises(Exception) as context:
            clscreen()
        self.assertIs(type(context.exception), TypeError)


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_clear_screen.py'], shell = True)