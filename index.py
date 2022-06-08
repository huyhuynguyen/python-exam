from time import sleep
import enums
import modules
import os
import subprocess
from modules.deck import Deck
from modules.house import House
from modules.log_mod import MyLogger
from modules.player import Player
from helpers.clear_screen import clear_screen as clscreen

class PlayingGuessGame:
    def __init__(self) -> None:
        self.player = Player()
        self.house = House()
        self.deck = Deck()
        self.point_target = 100
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
        while True:
            # clear screen
            run_command = clscreen()
            if (isinstance(run_command, subprocess.CalledProcessError)):
                print(run_command.stdout)

            print('-------------------- Start new round --------------------')
            if self.deck.is_out_of_card(): 
                break
            self.stage1()
            if self.is_auto_break_game():
                break

            # player choices
            print(''' 
                Your card is greater or less than house card? Choose one option:
                G (greater)
                L (less)
            ''')

            guess_choice = self.stage2()
            if guess_choice == ValueError:
                self.end_game_when_type_wrong()

            is_player_choose = self.stage3(guess_choice)
            self.player.print_card()
            if (is_player_choose):
                flag = self.player.is_continue()

                # decide continue or stop | point > target
                if (not flag) \
                    or self.is_auto_break_game():
                    break

                if flag == ValueError:
                    self.end_game_when_type_wrong()
            else:
                sleep(enums.TIME_SLEEP)
                
            sleep(enums.TIME_SLEEP)
        
        # clear screen
        run_command = clscreen()
        if (isinstance(run_command, subprocess.CalledProcessError)):
            print(run_command.stdout)
        # End game
        self.end_game()

    def end_game_when_type_wrong(self):
        MyLogger().print_log_wrong_option_console(enums.OUTPUT_TRY_TIMES)
        self.end_game()
        exit()

    def end_game(self):
        print('-------------------- End game --------------------')
        if self.deck.is_out_of_card():
            print('Out of card')

        print(f'Player point: {self.player.point}')
        result = 'wins!!' if self.player.point >= self.point_target else 'loses'
        print(f'You {result}')
        MyLogger().print_log_to_file(self.player.point, result, filename='my-log')


if __name__ == '__main__':
    PlayingGuessGame().start_game()
