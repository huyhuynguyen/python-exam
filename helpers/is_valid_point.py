def is_valid_point(func):
    def inner(self, point):
        if not isinstance(point, (int, float)):
            raise ValueError('Not valid point')

        return func(self, point)
    return inner