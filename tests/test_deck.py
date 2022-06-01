import unittest
import setup_path
from modules.deck import Deck
import subprocess

class TestDeck(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()

    def test_get_random_card(self):
        res = self.deck.get_random_card()
        self.assertIn(res['card'], self.deck.card_list)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_deck.py'], shell = True)