from io import StringIO
import setup_path
import unittest
from unittest.mock import patch
from helpers.clear_screen import clear_screen as clscreen
import subprocess
import sys

class TestClearScreen(unittest.TestCase):
    def test_is_clear_screen_called(self):
        with patch('helpers.clear_screen.subprocess.run') as mock_object:
            clscreen()
            mock_object.assert_called()
            mock_object.assert_called_with(['cls'], check=True, shell=True)

    def test_is_clear_screen_failed_print(self):
        with patch('helpers.clear_screen.subprocess.run', side_effect = subprocess.SubprocessError):
            captured_output = StringIO()
            sys.stdout = captured_output
            clscreen()
            self.assertEqual(captured_output.getvalue(), "Command not found\n")


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_clear_screen.py'], shell = True)