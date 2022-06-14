import functools

def is_valid_point(func):
    @functools.wraps(func)
    def inner(self, point):
        if not isinstance(point, (int, float)):
            print('Not valid point')
            return ValueError

        return func(self, point)
    return inner