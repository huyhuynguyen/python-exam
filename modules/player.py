from modules.not_valid_choice import NotValidChoice
from modules.user import User
from helpers.is_valid_input import is_valid_input
from helpers.is_valid_point import is_valid_point


class Player(User):
    def __init__(self) -> None:
        self._point = 60
        super().__init__()

    @property
    def point(self) -> int:
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

    def print_card(self):
        print(f'Player card: {self.card_name}')
        
    
    def player_guess_input(self):
        string = is_valid_input(pattern = r"^[g,l]{1,1}", label = 'Enter your choice: ')
        if string == NotValidChoice:
            return NotValidChoice
        return 'greater' if string in ['G', 'g'] else 'less'

    @is_valid_point
    def spend_cost_each_round(self, point_cost):
        self.point -= point_cost

    @is_valid_point
    def update_point_guess_right(self, point_win):
        self.point += point_win

    def is_continue(self):
        text = is_valid_input(pattern = r"^[y,n]{1,1}", label = 'Continue to play[y/n]: ')
        if text == NotValidChoice:
            return NotValidChoice
        return text in ['Y', 'y']