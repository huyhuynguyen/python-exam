import unittest
import setup_path
from modules import User
import subprocess

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()

    def test_print_card_None(self):
        a = self.user.print_card()
        self.assertIsNone(a)

if __name__ == '__main__':
    subprocess.run(['pytest', '-v', r'tests/test_user.py'], shell = True)