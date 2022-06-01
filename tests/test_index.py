import unittest
from unittest.mock import PropertyMock, patch
import setup_path
from index import PlayingGuessGame
import subprocess

class TestPlayGame(unittest.TestCase):
    def setUp(self) -> None:
        self.play_game = PlayingGuessGame()

    # mock property to test
    @patch('index.House.card_order', new_callable = PropertyMock, return_value = 20)
    @patch('index.Player.card_order', new_callable = PropertyMock, return_value = 30)
    def test_is_guess_right_greater_true(self, house_card_order, player_card_order):
        res = self.play_game.is_guess_right('greater')
        self.assertTrue(res)

    @patch('index.House.card_order', new_callable = PropertyMock, return_value = 20)
    @patch('index.Player.card_order', new_callable = PropertyMock, return_value = 10)
    def test_is_guess_right_less_true(self, house_card_order, player_card_order):
        res = self.play_game.is_guess_right('less')
        self.assertTrue(res)

    @patch('index.House.card_order', new_callable = PropertyMock, return_value = 20)
    @patch('index.Player.card_order', new_callable = PropertyMock, return_value = 10)
    def test_is_guess_right_less_false(self, house_card_order, player_card_order):
        res = self.play_game.is_guess_right('greater')
        self.assertFalse(res)

    @patch('index.Player.point', new_callable = PropertyMock, return_value = 20)
    def test_is_auto_break_game_break(self, point):
        res = self.play_game.is_auto_break_game()
        self.assertTrue(res)

    @patch('index.Player.point', new_callable = PropertyMock, return_value = 40)
    def test_is_auto_break_game_not_break(self, point):
        res = self.play_game.is_auto_break_game()
        self.assertFalse(res)

    @patch('index.PlayingGuessGame.is_guess_right', return_value = True)
    def test_stage_3_true(self, guess_right):
        res = self.play_game.stage3('abc')
        self.assertTrue(res)

    @patch('index.PlayingGuessGame.is_guess_right', return_value = False)
    def test_stage_3_false(self, guess_wrong):
        res = self.play_game.stage3('abc')
        self.assertFalse(res)

    

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_index.py'], shell = True)
