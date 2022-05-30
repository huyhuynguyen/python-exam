from time import sleep
from enums import GuessText
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

        house_card_name = self.player.card['card']

        print(f'House card: {house_card_name}')
        # print(f'House card: {self.house.card}')
        # print(f'Player card: {self.player.card}')

    def player_guess_input(self):
        string = input('Enter your choice: ')
        while True:
            if string not in [GuessText(text.value).name for text in GuessText]:
                print('Invalid choice. Please choose again')
                string = input('Enter your choice: ')
            else:
                break

        return GuessText[string].value

    def is_guess_right(self, guessing):
        house_card_order = self.house.card['order']
        player_card_order = self.player.card['order']

        return (guessing == GuessText.G.value and player_card_order > house_card_order) or (guessing == GuessText.L.value and player_card_order < house_card_order)

    def is_continue(self):
        text = input('Continue to play[y/n]: ')
        while True:
            if text not in ['Y', 'y', 'n', 'N']:
                text = input('Continue to play[y/n]: ')
            else:
                break

        return text in ['Y', 'y']

    def update_point_guess_right(self):
        self.player.point += self.point_win

    def spend_cost_each_round(self):
        self.player.point -= self.point_cost_each_round

    def start_game(self):
        # start log
        self.my_logger.config_log_to_file()

        while True:
            # clear screen
            os.system('cls')

            print('-------------------- Start new round --------------------')
            self.spend_cost_each_round()

            print(f'Player point: {self.player.point}')
            if self.player.point < self.point_min_lose:
                break

            # player and house receive card
            self.receive_card()

            # player choices
            print(''' 
                Your card is greater or less than house card? Choose one option:
                G (greater)
                L (less)
            ''')

            guess_choice = self.player_guess_input()
            print(f'You guess your card is {guess_choice} than house')

            if self.is_guess_right(guessing=guess_choice):
                print('You guess right!!!')
                self.update_point_guess_right()

                # decide continue or stop | point > target
                if (not self.is_continue()) or self.player.point >= self.point_target:
                    break
            else:
                print('You guess wrong')
                
            sleep(enums.TIME_SLEEP)
        
        os.system('cls')
        # End game
        self.end_game()

    def end_game(self):
        print('-------------------- End game --------------------')
        self.my_logger.logger.info(f'Player point: {self.player.point}')
        print(f'Player point: {self.player.point}')
        if self.player.point >= self.point_target:
            print('You win!!!')
            self.my_logger.logger.info(f'Player win')
        else:
            print('You lose')
            self.my_logger.logger.info(f'Player lose')



if __name__ == '__main__':
    PlayingGuessGame().start_game()
