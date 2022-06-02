import random

class Deck:
    def __init__(self) -> None:
        self.suites = ['spade', 'club', 'diamond', 'heart']
        self.groups = ['A'] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K']
        self.greatest_card = ['b-joker', 'r-joker']
        self._card_list = self.get_card_list()

    def get_card_list(self):
        return [str(x)+'-'+str(y) for x in self.groups for y in self.suites] \
                + self.greatest_card

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, new_card_list):
        self._card_list = new_card_list

    def out_of_card(self):
        return len(self.card_list) < 2

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

    def remove_existed_cards(self, *existed_cards):
        self.card_list = list(filter(lambda card_item: card_item not in existed_cards, self.card_list))

# if __name__ == '__main__':
#     deck = Deck()
#     for x in range(20):
#         a = deck.get_random_card()
#         b = deck.get_random_card(except_card_name=a['card'])
#         deck.remove_existed_cards(a['card'], b['card'])


#     print(len(deck.card_list))

