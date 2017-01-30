"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 30, 2017

    ProjectEuler Q-3 : get the largest prime factor of a number

    ref : https://projecteuler.net/problem=3

    e.g.
    python largest_prime_factor_q3.py
    Enter the value of N : 100
    Prime factors : [2, 5]
    Largest Prime Factor : 5
"""

from pgmath.prime import primeTillN


def prime_factors(N):
    limit = int(N ** 0.5) + 1
    factors = []
    for x in primeTillN(limit):
        if N % x == 0:
            factors.append(x)
    return factors

if __name__ == '__main__':
    N = input("Enter the value of N : ")
    factors = prime_factors(N)
    if factors:
        print "Prime factors : %s" % factors
        print "Largest Prime Factor : %d" % max(factors)
    else:
        print "%d is a prime no, so no factors" % (N)
