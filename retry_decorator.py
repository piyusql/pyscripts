import random
from functools import wraps


def retry(error_type, retries):
    """
        The decorator performs retry of the wrapped function
        with given exception type and retries number
        You can wrap your function with @retry(Exception, N)
    """
    def decorator(func):
        # to preserve the original function meta data we need to apply wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    f = func(*args, **kwargs)
                except error_type:
                    print("execption in try %d" % (i + 1))
                    continue
                else:
                    print("passed in try %d" % (i + 1))
                    return f
        return wrapper
    return decorator


@retry(ZeroDivisionError, 3)
def divide(x):
    "Randomly divide by 0 or 1"
    d = random.choice([0, 1])
    print("selected dividend/divisor : %d/%d" % (x, d))
    print("result : %s" % (x / d))


if __name__ == '__main__':
    print("Function `%s`\n\t%s" % (divide.__name__, divide.__doc__))
    for i in xrange(10):
        print("=-=" * 12)
        print("TEST :: %d" % (i + 1))
        divide(random.randint(1, 100))
