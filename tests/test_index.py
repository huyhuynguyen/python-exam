import time
import unittest
from unittest.mock import PropertyMock, patch
import setup_path
from modules.not_valid_choice import NotValidChoice
from index import PlayingGuessGame
import subprocess
import index
class TestPlayGame(unittest.TestCase):
    def setUp(self) -> None:
        self.play_game = PlayingGuessGame()

    # mock test
    def test_get_random_card_called(self):
        with patch('index.Deck.get_random_card') as mock_object:
            self.play_game.receive_card()
            mock_object.assert_called()

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
    @patch('index.PlayingGuessGame.end_game')
    def test_end_game_log_stream_called_when_type_wrong(self, end_game_mock ,exit_mock):
        with patch('index.MyLogger.print_log_wrong_option_console') as mock_object:
            self.play_game.end_game_when_type_wrong()
            mock_object.assert_called()
    
    def test_end_game_log_file_called(self):
        with patch('index.MyLogger.print_log_to_file') as mock_object:
            self.play_game.end_game()
            mock_object.assert_called()

    @patch('index.Player.player_guess_input')
    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.MyLogger.print_log_to_file')
    def test_is_continue_called_when_guess_right(self, mock_print_file ,mock_start_banner, mock_guess_input):
        with patch('index.PlayingGuessGame.is_guess_right', return_value = True):
            with patch('index.Player.is_continue', return_value = False) as mock_is_continue:
                self.play_game.start_game()
                mock_is_continue.assert_called()


    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.PlayingGuessGame.is_auto_break_game', return_value = True)
    @patch('index.PlayingGuessGame.end_game')
    @patch('index.PlayingGuessGame.stage1')
    @patch('index.time.sleep')
    def test_deck_init_when_out_of_card(self, mock_sleep, mock_stage1, mock_end_game, mock_auto_break, mock_start_banner):
        mock_sleep.side_effect = ['abc', Exception]
        with patch('index.Deck.is_out_of_card', return_value = True):
            with patch('index.Deck.__new__') as mock_init_deck:
                with self.assertRaises(Exception):
                    self.play_game.start_game()
                    mock_init_deck.assert_called_once()

    @patch('sys.stdout.write')
    @patch('helpers.clear_screen.clear_screen')
    def test_sleep_text_length_time(self, mock_cls, mock_sys_write):
        with patch('index.time.sleep') as mock_sleep:
            self.play_game.start_game_banner()
            self.assertEqual(mock_sleep.call_count, len(index.start_banner) + 1)  

    @patch('time.sleep', return_value = None)
    def test_print_time_when_lose(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            self.play_game.wait_next_round_when_lose()
            self.assertEqual(mock_print.call_count, index.enums.NEXT_ROUND_TIME_LOSE + 1)

    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.Deck.is_out_of_card', return_value = False)
    @patch('index.PlayingGuessGame.stage1')
    @patch('index.PlayingGuessGame.is_auto_break_game', return_value = False)
    @patch('index.PlayingGuessGame.stage3', return_value = True)
    @patch('index.PlayingGuessGame.end_game')
    def test_call_end_game_type_wrong(self, mock_end_game, 
                                            mock_stage3, 
                                            mock_auto_break, mock_stage1, mock_out_of_card, 
                                            mock_start_banner):
        with patch('index.Player.player_guess_input', return_value = NotValidChoice), \
            patch('index.Player.is_continue', return_value = False):
            with patch('index.PlayingGuessGame.end_game_when_type_wrong') as mock_end_type_invalid:
                self.play_game.start_game()
                mock_end_type_invalid.assert_called()


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_index.py'], shell = True)
