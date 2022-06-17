from io import StringIO
import sys
import unittest
from unittest.mock import PropertyMock, patch
import setup_path
from modules.not_valid_choice import NotValidChoice
import subprocess
from modules import Player

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

    @patch('builtins.input', return_value = 'Y')
    def test_player_continue_2(self, input):
        res = self.player.is_continue()
        self.assertTrue(res)

    @patch('builtins.input', return_value = 'n')
    def test_player_stop_1(self, input):
        res = self.player.is_continue()
        self.assertFalse(res)

    @patch('modules.Player.card_name', new_callable = PropertyMock, return_value = 'abc')
    def test_player_print_card(self, card_name_mock):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.player.print_card()
        self.assertEqual(captured_output.getvalue(), f"Player card: {card_name_mock.return_value}\n")

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_player.py'], shell = True)
