from functools import reduce, wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memoize
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n


def factorial1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
