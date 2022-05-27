class Player:
    def __init__(self) -> None:
        self._point = 60
        self._card = None

    @property
    def point(self) -> int:
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

    @property
    def card(self) -> str:
        return self._card

    @card.setter
    def card(self, card):
        self._card = card

if __name__ == '__main__':
    p = Player()
    # p.point = 20
    print(p.point)