from modules.player.player import Player


class RichPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.point = 80