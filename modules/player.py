from modules.user import User
import enums


class Player(User):
    def __init__(self) -> None:
        self._point = 60

    @property
    def point(self) -> int:
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

    def player_guess_input(self):
        string = input('Enter your choice: ')
        count_input = 0
        while count_input < 3:
            if string not in ['G', 'L']:
                print('Invalid choice. Please choose again')
                string = input('Enter your choice: ')
            else:
                break
            count_input += 1
        
        if count_input == 3:
            raise ValueError(enums.INVALID_INPUT)

        return 'greater' if string == 'G' else 'less'

    def spend_cost_each_round(self, point_cost):
        self.point -= point_cost

    def update_point_guess_right(self, point_win):
        self.point += point_win

    def is_continue(self):
        text = input('Continue to play[y/n]: ')
        count_input = 0
        while count_input < 3:
            if text not in ['Y', 'y', 'n', 'N']:
                text = input('Continue to play[y/n]: ')
            else:
                break
            count_input += 1
        
        if count_input == 3:
            raise ValueError(enums.INVALID_INPUT)

        return text in ['Y', 'y']

if __name__ == '__main__':
    p = Player()
    # p.point = 20
    print(p.point)