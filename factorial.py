from functools import wraps

ITER = 0


def memoize(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

#@memoize


def fact(n):
    global ITER
    ITER += 1
    if n <= 1:
        return 1
    return fact(n - 1) * n

if __name__ == '__main__':
    N = input("Enter range : ")
    Y = raw_input("Use calculated, (y/n) : ")
    if Y == 'y':
        fact = memoize(fact)
    print "Number\tIteration\tFactorial\n", "-" * 32
    for i in range(1, N + 1):
        print "%5d\t%9d\t%d" % (i, ITER, fact(i))
