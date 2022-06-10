from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self) -> None:
        self._card = {
            'card': None,
            'order': None
        }

    @property
    def card(self) -> str:
        return self._card

    @card.setter
    def card(self, card): 
        self._card = card

    @property
    def card_order(self):
        return self.card['order']

    @property
    def card_name(self):
        return self.card['card']

    @abstractmethod
    def print_card(self):
        # implement in child class
        pass