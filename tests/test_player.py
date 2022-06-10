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

    @patch('modules.player.is_valid_input', return_value = NotValidChoice)
    def test_player_guess_input_falied(self, string_mock):
        res = self.player.player_guess_input()
        self.assertIs(res, string_mock.return_value)

    @patch('builtins.input', return_value = 'Y')
    def test_player_continue_2(self, input):
        res = self.player.is_continue()
        self.assertTrue(res)

    @patch('builtins.input', return_value = 'n')
    def test_player_stop_1(self, input):
        res = self.player.is_continue()
        self.assertFalse(res)

    @patch('modules.player.is_valid_input', return_value = NotValidChoice)
    def test_player_is_continue_falied(self, string_mock):
        res = self.player.is_continue()
        self.assertIs(res, string_mock.return_value)

    @patch('modules.Player.card_name', new_callable = PropertyMock, return_value = 'abc')
    def test_player_print_card(self, card_name_mock):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.player.print_card()
        self.assertEqual(capturedOutput.getvalue(), f"Player card: {card_name_mock.return_value}\n")

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_player.py'], shell = True)
