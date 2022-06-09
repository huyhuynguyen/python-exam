import unittest
from unittest.mock import PropertyMock, patch
import setup_path
from index import PlayingGuessGame
import subprocess
class TestPlayGame(unittest.TestCase):
    def setUp(self) -> None:
        self.play_game = PlayingGuessGame()

    # mock test
    def test_get_random_card_called(self):
        with patch('index.Deck.get_random_card') as mock_object:
            self.play_game.receive_card()
            mock_object.assert_called()

    # # mock property to test
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

    def test_stage1_subtract_point_called(self):
        with patch('index.Player.spend_cost_each_round') as sub_point_mock, \
            patch('index.PlayingGuessGame.receive_card') as receive_mock:
            self.play_game.stage1()
            sub_point_mock.assert_called()
            receive_mock.assert_called()

    def test_stage2_player_guess_called(self):
        with patch('index.Player.player_guess_input') as mock_object:
            self.play_game.stage2()
            mock_object.assert_called()

    @patch('index.PlayingGuessGame.is_guess_right', return_value = True)
    def test_stage_3_true(self, guess_right, ):
        with patch('index.Player.update_point_guess_right') as mock_object:
            res = self.play_game.stage3('abc')
            mock_object.assert_called()
        self.assertTrue(res)

    @patch('index.PlayingGuessGame.is_guess_right', return_value = False)
    def test_stage_3_false(self, guess_wrong):
        with patch('index.Player.update_point_guess_right') as mock_object:
            res = self.play_game.stage3('abc')
            mock_object.assert_not_called()
        self.assertFalse(res)

    @patch('builtins.exit')
    def test_end_game_log_stream_called_when_type_wrong(self, exit_mock):
        with patch('index.MyLogger.print_log_wrong_option_console') as mock_object:
            self.play_game.end_game_when_type_wrong()
            mock_object.assert_called()
    
    def test_end_game_log_file_called(self):
        with patch('index.MyLogger.print_log_to_file') as mock_object:
            self.play_game.end_game()
            mock_object.assert_called()

    @patch('index.Player.player_guess_input')
    @patch('index.PlayingGuessGame.start_game_banner')
    def test_is_continue_called_when_guess_right(self, mock_start_banner, mock_guess_input):
        with patch('index.PlayingGuessGame.is_guess_right', return_value = True) as mock_is_guess_right:
            with patch('index.Player.is_continue', return_value = False) as mock_is_continue:
                self.play_game.start_game()
                mock_is_continue.assert_called()


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_index.py'], shell = True)
