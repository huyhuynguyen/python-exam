import random

class Deck:
    def __init__(self) -> None:
        self.suites = ['spade', 'club', 'diamond', 'heart']
        self.groups = ['A'] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K']
        self.greatest_card = ['b-joker', 'r-joker']

    @property
    def suites_group(self):
        return [str(x)+'-'+str(y) for x in self.groups for y in self.suites]

    @property
    def card_list(self):
        return self.suites_group + self.greatest_card

    # bug: duplicate card when random
    def get_random_card(self, except_card_name = None):
        card_list = self.card_list.copy()
        if except_card_name:
            card_list = [card for card in card_list if card != except_card_name]
        card: str = random.choice(card_list)
        index: int = card_list.index(card)
        return {
            'card': card,
            'order': index
        }

if __name__ == '__main__':
    print(Deck().card_list)

