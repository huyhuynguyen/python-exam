import enums

class NotValidPoint(Exception):
    def __str__(self) -> str:
        return enums.OUTPUT_GAME_POINT_ERROR