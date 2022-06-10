import unittest
from unittest.mock import PropertyMock, patch
import setup_path
from modules import User
import subprocess

class TestUser(unittest.TestCase):
    @patch("modules.User.__abstractmethods__", set())
    def test_get_card_order(self):
        card = {
            'card': 'a',
            'order': 10
        }
        with patch('modules.User.card', new_callable=PropertyMock, return_value = card) as mock_card:
            user = User()
            card_order = user.card_order
            self.assertEqual(card_order, mock_card.return_value['order'])

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_user.py'], shell = True)