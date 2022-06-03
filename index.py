import subprocess
from time import sleep
import enums
import modules
import os
from modules.deck import Deck
from modules.house import House
from modules.log_mod import MyLogger
from modules.player import Player

class PlayingGuessGame:
    def __init__(self) -> None:
        self.player = Player()
        self.house = House()
        self.deck = Deck()
        self.my_logger = MyLogger()
        self.point_target = 100
        self.point_cost_each_round = 10
        self.point_win = 20
        self.point_min_lose = 30

    def receive_card(self):
        self.house.card = self.deck.get_random_card()
        self.player.card = self.deck.get_random_card()

        self.house.print_card()

        # print(f'House card: {self.house.card}')
        # print(f'Player card: {self.player.card}')

    def is_guess_right(self, guessing):
        house_card_order = self.house.card_order
        player_card_order = self.player.card_order

        return ((guessing == enums.GuessText.G.value and player_card_order > house_card_order) \
                    or (guessing == enums.GuessText.L.value and player_card_order < house_card_order))

    def is_auto_break_game(self):
        return self.player.point not in \
                range(self.point_min_lose, self.point_target+1) \
                or self.deck.is_out_of_card()

    def clear_screen(self):
        command = enums.CLS_COMMAND_WINDOWS
        try:
            subprocess.run(command, check=True, shell = True)
        except:
            raise TypeError(f'"{"".join(command)}" command does not exist')

    def stage1(self):
        self.player.spend_cost_each_round(self.point_cost_each_round)
        print(f'Player point: {self.player.point}')

        # player and house receive card
        self.receive_card()

    def stage2(self):
        guess_choice = self.player.player_guess_input()
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
        # start log
        self.my_logger.config_log_to_file()

        while True:
            # clear screen
            self.clear_screen()

            print('-------------------- Start new round --------------------')
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

            is_player_choose = self.stage3(guess_choice)
            if (is_player_choose):
                # decide continue or stop | point > target
                if (not self.player.is_continue()) \
                    or self.is_auto_break_game():
                    break
                
            sleep(enums.TIME_SLEEP)
        
        self.clear_screen()
        # End game
        self.end_game()

    def end_game(self):
        print('-------------------- End game --------------------')
        self.deck.is_out_of_card()

        print(f'Player point: {self.player.point}')
        result = 'wins!!' if self.player.point >= self.point_target else 'loses'
        print(f'You {result}')
        self.my_logger.print_log_to_file(self.player.point, result)


if __name__ == '__main__':
    PlayingGuessGame().start_game()
