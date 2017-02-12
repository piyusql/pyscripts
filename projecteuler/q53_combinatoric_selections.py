"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 12, 2017

    ProjectEuler Q-53 : combinations limit

    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5C3 = 10.

    In general, nCr = n!/r!/(n-r)!
    where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.

    It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

    How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

    ref : https://projecteuler.net/problem=52

    e.g
    >>> time python q53_combinatoric_selections.py
    Enter value of N for nCr : 100
    Enter limit to check : 1000000
    Total result count : 4075

    real    0m5.394s
    user    0m0.028s
    sys     0m0.005s

    >>> time python q53_combinatoric_selections.py
    Enter value of N for nCr : 1000
    Enter limit to check : 1000000000
    Total result count : 491894

    real    0m31.728s
    user    0m19.827s
    sys     0m0.176s
    """

from pgmath.combinations import ncr


def check(N, M):
    values = []
    for n in xrange(1, N + 1):
        for r in xrange(1, n // 2 + 1):
            val = ncr(n, r)
            if val > M:
                values.append((n, r, val))
                if n - r > r:
                    values.append((n, n - r, val))
    return values

if __name__ == '__main__':
    N = input("Enter value of N for nCr : ")
    M = input("Enter limit to check : ")
    print "Total result count : %d" % len(check(N, M))
