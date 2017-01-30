"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 31, 2017

    ProjectEuler Q-5 : get the least common multiple (lcm) of given number

    ref : https://projecteuler.net/problem=5

    e.g.
    >>> python q5_least_common_multiple.py
    Enter the value of N : 10
    Largest common multiple : 2520
    >>> python q5_least_common_multiple.py
    Enter the value of N : 20
    Largest common multiple : 232792560
    >>> python q5_least_common_multiple.py
    Enter the value of N : 30
    Largest common multiple : 2329089562800
    >>> python q5_least_common_multiple.py
    Enter the value of N : 40
    Largest common multiple : 5342931457063200
    >>> python q5_least_common_multiple.py
    Enter the value of N : 50
    Largest common multiple : 3099044504245996706400
"""
from functools import reduce


def gcd(*args):
    def _gcd(x, y):
        if x > y:
            lead = x
            factor = y
        else:
            lead = y
            factor = x
        while(factor > 0):
            lead, factor = factor, lead % factor
        return lead
    return reduce(_gcd, args)


def lcm(*args):
    def _lcm(x, y):
        return x * y / gcd(x, y)
    return reduce(lambda x, y: _lcm(x, y), args)

if __name__ == '__main__':
    N = input("Enter the value of N : ")
    print "Largest common multiple : %s" % lcm(* range(1, N + 1))
