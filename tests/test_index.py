import unittest
import index

class TestPlayerGuess(unittest.TestCase):
    def setUp(self) -> None:
        self.play_game = index.PlayingGuessGame()

    def test_player_guess_input_greater(self):
        res = self.play_game.player_guess_input('G')
        expected = 'greater'
        self.assertEqual(res, expected)

    def test_player_guess_input_less(self):
        res = self.play_game.player_guess_input('L')
        expected = 'less'
        self.assertEqual(res, expected)

    def test_player_enter_fail_choice(self):
        res = self.play_game.player_guess_input('A')
        