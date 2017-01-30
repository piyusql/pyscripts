"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 31, 2017

    ProjectEuler Q-6 : get the difference of sum of squares in series
        and square of sum of integers in series
    diff( (1 + 2 + 3 ...)^2 - (1^2 + 2^2 + 3^2 + ...) )

    ref : https://projecteuler.net/problem=6

    e.g.
    >>> python q6_sum_square_difference.py
    Enter the value of N : 10
    Diff : 2640
    >>> python q6_sum_square_difference.py
    Enter the value of N : 100
    Diff : 25164150
    >>> python q6_sum_square_difference.py
    Enter the value of N : 1000
    Diff : 250166416500
    >>> python q6_sum_square_difference.py
    Enter the value of N : 10000
    Diff : 2500166641665000
    >>> python q6_sum_square_difference.py
    Enter the value of N : 100000
    Diff : 25000166664166650000
    >>> python q6_sum_square_difference.py
    Enter the value of N : 1000000
    Diff : 250000166666416666500000
    >>> python q6_sum_square_difference.py
    Enter the value of N : 10000000
    Diff : 2500000166666641666665000000
"""


def diff(N):
    sum_of_squares = sum(x * x for x in range(1, N + 1))
    squares_of_sum = sum(x for x in range(1, N + 1)) ** 2
    return squares_of_sum - sum_of_squares

if __name__ == '__main__':
    N = input("Enter the value of N : ")
    print "Diff : %d" % diff(N)
