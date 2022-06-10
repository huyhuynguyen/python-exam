import enums

class NotValidChoice(Exception):
    def __str__(self) -> str:
        return enums.INVALID_INPUT