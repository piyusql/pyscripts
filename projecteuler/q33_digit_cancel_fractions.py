"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 18, 2017

    ProjectEuler Q-33 : digit cancelling fractions

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, less than
    one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.

    ref : https://projecteuler.net/problem=33
"""


import copy
import operator
from fractions import Fraction
from functools import reduce


def main():
    fractions = []
    for n in range(11, 100):
        ns = [n1 for n1 in str(n)]
        for d in range(n + 1, 100):
            ds = [d1 for d1 in str(d)]
            common = [x for x in ns if x in ds]
            if len(common) == 1:
                common = common[0]
                if common == '0':
                    continue
                ns1 = copy.copy(ns)
                ns1.remove(common)
                ds.remove(common)
                if d != 0 and ds[0] != '0' and Fraction(
                        n, d) == Fraction(int(ns1[0]), int(ds[0])):
                    fractions.append(Fraction(n, d))
    print "Product of fractions : ", reduce(operator.mul, fractions)

if __name__ == '__main__':
    main()
