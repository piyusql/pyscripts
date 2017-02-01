"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 1, 2017

    ProjectEuler Q-16 : finding sun of digits in resulting N power to 2

    ref : https://projecteuler.net/problem=16

    e.g.
    >>> python q16_power_digits_sum.py
    Enter the power raised to value 2 : 10
    Sum of digits in (2^10) is 7.
    >>> python q16_power_digits_sum.py
    Enter the power raised to value 2 : 100
    Sum of digits in (2^100) is 115.
    >>> python q16_power_digits_sum.py
    Enter the power raised to value 2 : 1000
    Sum of digits in (2^1000) is 1366.
"""


if __name__ == '__main__':
    X = 2
    N = input("Enter the power raised to value %d : " % (X))
    value = X ** N
    _sum = sum(int(char) for char in str(value))
    print "Sum of digits in (%d^%d) is %d." % (X, N, _sum)
