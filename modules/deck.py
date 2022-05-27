import random

class Deck:
    def __init__(self) -> None:
        self.suites = ['spade', 'club', 'diamond', 'heart']
        self.groups = ['A'] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K']
        self.greatest_card = ['b-joker', 'r-joker']

    @property
    def suites_group(self) -> list:
        return [str(x)+'-'+str(y) for x in self.groups for y in self.suites]

    def get_random_card(self) -> dict:
        card_list: list = self.suites_group + self.greatest_card
        card: str = random.choice(card_list)
        index: int = card_list.index(card)
        return {
            'card': card,
            'order': index
        }

if __name__ == '__main__':
    print(Deck().get_random_card())

