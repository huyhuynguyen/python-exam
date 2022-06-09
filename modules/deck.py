import random

class Deck:
    def __init__(self) -> None:
        self.suites = ['\u2660', '\u2663', '\u2666', '\u2665']
        self.groups = ['A'] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K']
        self.greatest_card = ['b-joker', 'r-joker']
        self._card_list = self.get_card_list()

    def get_card_list(self):
        card_list_name = [str(x)+str(y) for x in self.groups for y in self.suites] \
                + self.greatest_card

        return [{
            'card': item,
            'order': index
        } for index, item in enumerate(card_list_name)]

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, new_card_list):
        self._card_list = new_card_list

    def is_out_of_card(self):
        return len(self.card_list) < 2

    def get_random_card(self):
        card = random.choice(self.card_list)
        # remove card after choose
        self.card_list.remove(card)
        return card
