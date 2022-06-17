import re
import time
import enums
import os
import sys
import time
from modules.deck import Deck
from modules.factory.poor_player_factory import PoorPlayerFactory
from modules.factory.rich_player_factory import RichPlayerFactory
from modules.house import House
from modules.log_mod import MyLogger
from modules.not_valid_choice import NotValidChoice
from modules.player import Player
from helpers.clear_screen import clear_screen as clscreen
from helpers import is_valid_input
from modules.player.player import Player


start_banner = "Welcome to guessing game"
logging_filename = 'my-log'
game_question = ''' 
                Your card is greater or less than house card? Choose one option:
                G (greater)
                L (less)
            '''
class PlayingGuessGame:
    def __init__(self) -> None:
        self.player = None
        self.house = House()
        self.deck = Deck()
        self.point_target = 120
        self.point_cost_each_round = 10
        self.point_win = 20
        self.point_min_lose = 30

    def receive_card(self):
        self.house.card = self.deck.get_random_card()
        self.player.card = self.deck.get_random_card()

        self.house.print_card()

    def is_guess_right(self, guessing):
        house_card_order = self.house.card_order
        player_card_order = self.player.card_order

        return ((guessing == enums.GuessText.G.value and player_card_order > house_card_order) \
                    or (guessing == enums.GuessText.L.value and player_card_order < house_card_order))

    def is_auto_break_game(self):
        return self.player.point not in \
                range(self.point_min_lose, self.point_target+1)
    
    def start_game_banner(self):
        # clear screen
        clscreen()
        for index, character in enumerate(start_banner):
            if index == len(start_banner) - 1:
                print(character, end='\n')
            else:
                sys.stdout.write(character)
                sys.stdout.flush()
            time.sleep(enums.TEXT_RUNNING)

        print("Start game")
        time.sleep(enums.WAITING_NEXT_ROUND)

    def choose_player_type(self):
        while True:
            print('-------------------- Choose player --------------------')
            print('1. Poor player')
            print('2. Rich player')
            pattern = re.compile(r'^[12]')
            text = is_valid_input.is_valid_input(pattern, label='Choose your player: ', ignore_case_flag=False)
            if text == NotValidChoice:
                continue
            else:
                # create player factory
                if text == '1':
                    factory = PoorPlayerFactory()
                else:
                    factory = RichPlayerFactory()

                self.player: Player = factory.create_player()
                if isinstance(self.player, (Player)):
                    break

    def wait_next_round_when_lose(self):
        # print 3 2 1 .... -> next round
        for second in range(enums.NEXT_ROUND_TIME_LOSE):
            print(f'Waiting ... {enums.NEXT_ROUND_TIME_LOSE-second}', end='\r') # cursor at start line
            time.sleep(enums.WAITING_TIME_LOSE)
        else:
            sys.stdout.write("\033[K") # clear line
            print('Next round')

    def stage1(self):
        self.player.spend_cost_each_round(self.point_cost_each_round)
        print(f'Player point: {self.player.point}')

        # player and house receive card
        self.receive_card()

    def stage2(self):
        guess_choice = self.player.player_guess_input()
        if isinstance(guess_choice, str):
            print(f'You guess your card is {guess_choice} than house')
        return guess_choice

    def stage3(self, guess_choice):
        if self.is_guess_right(guessing = guess_choice):
            print('You guess right!!!')
            self.player.update_point_guess_right(self.point_win)

            return True

        print('You guess wrong')
        return False

    def start_game(self):
        # Start game banner
        self.start_game_banner()

        # Choose player type
        self.choose_player_type()

        while True:
            # clear screen
            clscreen()

            print('-------------------- Start new round --------------------')
            if self.deck.is_out_of_card(): 
                print('Out of card!!!')
                print('Start again')
                self.deck = Deck()
                time.sleep(enums.WAITING_NEXT_ROUND)
                continue
            
            self.stage1()
            if self.is_auto_break_game():
                break

            # player choices
            print(game_question)

            guess_choice = self.stage2()
            if guess_choice == NotValidChoice:
                self.end_game_when_type_wrong()

            is_player_choose_right = self.stage3(guess_choice)
            self.player.print_card()
            if (is_player_choose_right):
                flag = self.player.is_continue()

                if flag == NotValidChoice:
                    self.end_game_when_type_wrong()

                # decide continue or stop | point > target
                if (not flag) \
                    or self.is_auto_break_game():
                    break

            else:
                self.wait_next_round_when_lose()

            time.sleep(enums.WAITING_NEXT_ROUND)
        
        # clear screen
        clscreen()
        # End game
        self.end_game()

    def end_game_when_type_wrong(self):
        MyLogger().print_log_wrong_option_console(enums.OUTPUT_TRY_TIMES)
        self.end_game()
        exit()

    def end_game(self):
        print('-------------------- End game --------------------')
        print(f'Player point: {self.player.point}')
        result = 'wins!!' if self.player.point >= self.point_target else 'loses'
        print(f'You {result}')
        MyLogger().print_log_to_file(self.player.point, result, filename=logging_filename)


if __name__ == '__main__':
    PlayingGuessGame().start_game()
