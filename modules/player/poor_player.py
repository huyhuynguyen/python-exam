from modules.player.player import Player


class PoorPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.point = 60