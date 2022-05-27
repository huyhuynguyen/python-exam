class House:
    def __init__(self) -> None:
        self._card = None

    @property
    def card(self) -> str:
        return self._card

    @card.setter
    def card(self, card): 
        self._card = card

if __name__ == '__main__':
    pass