from modules.user import User
import enums
import re


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

    def player_guess_input(self):
        count_input = 0
        pattern = re.compile(r"^[g,l]{1,1}", re.IGNORECASE)
        while True:
            if count_input == enums.TRY_TIME:
                raise ValueError(enums.INVALID_INPUT)

            string = input('Enter your choice: ')
            # if string not in ['G', 'L', 'g', 'l']:
            if not re.fullmatch(pattern, string):
                count_input += 1
                print(f'Invalid choice. Please choose again. {enums.TRY_TIME - count_input} times try')
            else:
                break

        return 'greater' if string == 'G' else 'less'

    def spend_cost_each_round(self, point_cost):
        self.point -= point_cost

    def update_point_guess_right(self, point_win):
        self.point += point_win

    def is_continue(self):
        count_input = 0
        pattern = re.compile(r"^[y,n]{1,1}", re.IGNORECASE)
        while True:
            if count_input == enums.TRY_TIME:
                raise ValueError(enums.INVALID_INPUT)

            text = input('Continue to play[y/n]: ')
            # if text not in ['Y', 'y', 'n', 'N']:
            if not re.fullmatch(pattern, text):
                count_input += 1
                print(f'Invalid choice. Please choose again. {enums.TRY_TIME - count_input} times try')
            else:
                break

        return text in ['Y', 'y']

# if __name__ == '__main__':
#     p = Player()
#     # p.point = 20
#     print(p.point)