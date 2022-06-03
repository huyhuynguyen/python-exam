from io import StringIO
import unittest
from unittest.mock import PropertyMock, patch

from pyparsing import sys
import setup_path
from modules.deck import Deck
import subprocess

class TestDeck(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()

    def test_get_random_card(self):
        res = self.deck.get_random_card()
        self.assertNotIn(res['card'], self.deck.card_list)

    @patch.object(Deck, 'card_list', new_callable = PropertyMock, return_value = [])
    def test_print_if_out_card(self, card_list_mock):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.deck.is_out_of_card()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Out of card\n")


if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_deck.py'], shell = True)