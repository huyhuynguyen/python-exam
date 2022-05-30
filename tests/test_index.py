import unittest
import setup_path
import index

class TestPlayerGuess(unittest.TestCase):
    def setUp(self) -> None:
        self.play_game = index.PlayingGuessGame()

    def test_player_guess_input_greater(self):
        res = self.play_game.player_guess_input()
        expected = 'greater'
        self.assertEqual(res, expected)

    def test_player_guess_input_less(self):
        res = self.play_game.player_guess_input()
        expected = 'less'
        self.assertEqual(res, expected)

    def test_player_continue(self):
        res = self.play_game.is_continue()
        self.assertTrue(res)

    def test_player_stop(self):
        res = self.play_game.is_continue()
        self.assertFalse(res)
