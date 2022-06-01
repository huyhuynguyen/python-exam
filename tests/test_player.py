import unittest
from unittest.mock import patch
import setup_path
import subprocess
from modules.player import Player

class TestPlayerGuess(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()

    @patch('builtins.input', return_value = 'G')
    def test_player_guess_input_greater(self, input):
        res = self.player.player_guess_input()
        expected = 'greater'
        self.assertEqual(res, expected)

    @patch('builtins.input', return_value = 'L')
    def test_player_guess_input_less(self, input):
        res = self.player.player_guess_input()
        expected = 'less'
        self.assertEqual(res, expected)

    @patch('builtins.input', return_value = 'y')
    def test_player_continue_1(self, input):
        res = self.player.is_continue()
        self.assertTrue(res)

    @patch('builtins.input', return_value = 'Y')
    def test_player_continue_2(self, input):
        res = self.player.is_continue()
        self.assertTrue(res)

    @patch('builtins.input', return_value = 'n')
    def test_player_stop_1(self, input):
        res = self.player.is_continue()
        self.assertFalse(res)

    @patch('builtins.input', return_value = 'N')
    def test_player_stop_2(self, input):
        res = self.player.is_continue()
        self.assertFalse(res)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_player.py'], shell = True)
