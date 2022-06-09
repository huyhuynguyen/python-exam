import unittest
from unittest.mock import PropertyMock, patch
import setup_path
from modules import Deck
import subprocess

class TestDeck(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()

    def test_get_random_card(self):
        res = self.deck.get_random_card()
        self.assertNotIn(res['card'], self.deck.card_list)

    @patch('modules.Deck.card_list', new_callable = PropertyMock, return_value = [])
    def test_out_of_card_True(self, card_list_mock):
        self.assertTrue(self.deck.is_out_of_card())


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_deck.py'], shell = True)