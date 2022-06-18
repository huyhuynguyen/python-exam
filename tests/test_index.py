import setup_path
import time
import unittest
from unittest.mock import PropertyMock, patch
from modules.not_valid_point import NotValidPoint
from modules.not_valid_choice import NotValidChoice
from index import PlayingGuessGame
import subprocess
import index
class TestPlayGame(unittest.TestCase):
    def setUp(self) -> None:
        self.play_game = PlayingGuessGame()

    def test_get_random_card_called(self):
        with patch('index.Deck.get_random_card') as mock_get_random_card:
            self.play_game.receive_card()
            mock_get_random_card.assert_called()
            self.assertEqual(mock_get_random_card.call_count, 2)

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
        with patch('index.Player.spend_cost_each_round') as mock_sub_point, \
            patch('index.PlayingGuessGame.receive_card') as mock_receive_card:
            self.play_game.stage1()
            mock_sub_point.assert_called()
            mock_receive_card.assert_called()

    def test_stage2_player_guess_called(self):
        with patch('index.Player.player_guess_input') as mock_guess_input:
            self.play_game.stage2()
            mock_guess_input.assert_called()

    @patch('index.PlayingGuessGame.is_guess_right', return_value = True)
    def test_stage_3_true(self, guess_right):
        with patch('index.Player.update_point_guess_right') as mock_update_point_guess_right:
            res = self.play_game.stage3('abc')
            mock_update_point_guess_right.assert_called()
            self.assertEqual(res, True)

    @patch('index.PlayingGuessGame.is_guess_right', return_value = False)
    def test_stage_3_false(self, guess_wrong):
        with patch('index.Player.update_point_guess_right') as mock_update_point_guess_right:
            res = self.play_game.stage3('abc')
            mock_update_point_guess_right.assert_not_called()
            self.assertEqual(res, False)

    @patch('index.PlayingGuessGame.end_game')
    def test_end_game_log_stream_called_when_type_wrong(self, 
                                                        mock_end_game):
        message = 'message'
        with patch('index.MyLogger.print_log_wrong_option_console') \
                as mock_print_log_console:
            self.play_game.end_game_when_exception(message)
            mock_print_log_console.assert_called()
            mock_print_log_console.assert_called_with('message')
    
    @patch('builtins.exit')
    def test_end_game_log_file_called(self, mock_exit):
        with patch('index.MyLogger.print_log_to_file') as mock_log_file:
            self.play_game.end_game()
            mock_log_file.assert_called()

    @patch('index.PlayingGuessGame.stage2')
    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.PlayingGuessGame.end_game')
    @patch('time.sleep')
    def test_is_continue_called_when_guess_right(self, mock_sleep, 
                                                        mock_end_game, 
                                                        mock_start_banner, 
                                                        mock_stage_2):
        with patch('index.PlayingGuessGame.is_guess_right', return_value = True):
            with patch('index.Player.is_continue', return_value = False) as mock_is_continue:
                self.play_game.start_game()
                mock_is_continue.assert_called()

    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.Deck.is_out_of_card', return_value = True)
    @patch('index.PlayingGuessGame.is_auto_break_game', return_value = True)
    @patch('index.PlayingGuessGame.end_game')
    @patch('index.PlayingGuessGame.stage1')
    @patch('time.sleep')
    def test_deck_init_when_out_of_card(self, mock_sleep, 
                                                mock_stage1, 
                                                mock_end_game, 
                                                mock_auto_break, 
                                                mock_is_out_of_card,
                                                mock_start_banner):
        mock_sleep.side_effect = ['abc', OSError]
        with patch('index.Deck.is_out_of_card', return_value = True):
            with patch('index.Deck.__new__') as mock_init_deck:
                with self.assertRaises(OSError):
                    self.play_game.start_game()
                mock_init_deck.assert_called()

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
    @patch('index.PlayingGuessGame.is_auto_break_game')
    @patch('index.PlayingGuessGame.stage3', return_value = True)
    @patch('index.PlayingGuessGame.end_game', side_effect = NotValidChoice)
    @patch('index.PlayingGuessGame.stage2')
    def test_call_end_game_type_wrong(self, 
                                            mock_stage2, 
                                            mock_end_game, 
                                            mock_stage3, 
                                            mock_auto_break, 
                                            mock_stage1, 
                                            mock_out_of_card, 
                                            mock_start_banner):
        mock_auto_break.side_effect = [False, True]
        mock_stage2.side_effect = [NotValidChoice, 'abc']

        with patch('index.PlayingGuessGame.end_game_when_exception') as mock_end_type_invalid:
            with self.assertRaises(NotValidChoice):
                self.play_game.start_game()
            mock_end_type_invalid.assert_called()

    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.Deck.is_out_of_card', return_value = False)
    @patch('index.PlayingGuessGame.is_auto_break_game', return_value = True)
    @patch('index.PlayingGuessGame.stage1')
    @patch('index.PlayingGuessGame.end_game', side_effect = NotValidPoint)
    def test_call_end_game_not_valid_point(self, mock_end_game,
                                                    mock_stage1, 
                                                    mock_auto_break,
                                                    mock_out_of_card, 
                                                    mock_start_banner):
        
        mock_stage1.side_effect = [NotValidPoint, 'abc']
        with patch('index.PlayingGuessGame.end_game_when_exception') as mock_end_type_invalid:
            with self.assertRaises(NotValidPoint):
                self.play_game.start_game()
            mock_end_type_invalid.assert_called()

    @patch('index.PlayingGuessGame.start_game_banner')
    @patch('index.Deck.is_out_of_card', return_value = False)
    @patch('index.PlayingGuessGame.is_auto_break_game')
    @patch('index.PlayingGuessGame.stage3', return_value = False)
    @patch('index.PlayingGuessGame.stage2')
    @patch('index.PlayingGuessGame.stage1')
    @patch('index.PlayingGuessGame.end_game')
    def test_wait_next_round_when_lose(self, mock_end_game,
                                                mock_stage1, 
                                                mock_stage2,
                                                mock_stage3,
                                                mock_auto_break,
                                                mock_out_of_card, 
                                                mock_start_banner):
        
        mock_auto_break.side_effect = [False, True]
        with patch('index.PlayingGuessGame.wait_next_round_when_lose') as mock_wait_lose:
            self.play_game.start_game()
            mock_wait_lose.assert_called()



if __name__ == '__main__':
    # unittest.main()
    subprocess.run(['pytest', '-v', r'tests/test_index.py'], shell = True)
