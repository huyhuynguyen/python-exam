from modules.factory.player_factory import PlayerFactory
from modules.player.poor_player import PoorPlayer


class PoorPlayerFactory(PlayerFactory):
    def create_player(self):
        return PoorPlayer()