import re
from helpers.is_valid_input import is_valid_input
from modules.factory.player_factory import PlayerFactory
from modules.not_valid_choice import NotValidChoice
from modules.player.rich_player import RichPlayer


class RichPlayerFactory(PlayerFactory):
    def create_player(self):
        # Enter secret word
        pattern = re.compile(r'secret')
        text = is_valid_input(pattern, 'Enter secret word: ', ignore_case_flag=False)
        if text == NotValidChoice:
            return None
        return RichPlayer()