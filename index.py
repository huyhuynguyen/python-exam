import modules
from modules.house import House
from modules.player import Player

class PlayingGuessGame:
    def __init__(self) -> None:
        self.player = Player()
        self.house = House()

    def player_guess_input(self, test_character = None):
        pass

    def start_game(self):
        pass
        

print(modules.Deck().suites_group)
