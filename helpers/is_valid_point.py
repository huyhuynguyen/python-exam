import functools
from modules.not_valid_point import NotValidPoint

def is_valid_point(func):
    @functools.wraps(func)
    def inner(self, point):
        if not isinstance(point, (int, float)):
            raise NotValidPoint

        return func(self, point)
    return inner