"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Sep 30, 2017

    ProjectEuler Q-39 : Integer right triangles

    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?

    e.g.
    >>> $ /usr/bin/time python q039_integer_right_triangles.py
    Enter max value for p : 1000
    Max no of solution exists for number 840
            2.26 real         0.04 user         0.00 sys
"""

import math


def solution_exists(p, a):
    """
    We know that a <= b < c and all are integers
    a^2 + b^2 = c^2 (1)
    a + b + c = p (2)
    => c = p - (a + b)
    We have values of p and a, lets find b in terms of p and a
    If any b exists with the integer value will be the part of solution.

    => a^2 + b^2 = (p - (a+b))^2
    => a^2 + b^2 = p^2 -2p(a+b) + a^2 + b^2 + 2ab
    => p^2 - 2pa = 2pb - 2ab
    => b = (p^2-2pa)/2(p-a)
    """
    return (p**2 - 2 * p * a) % (2 * (p - a)) == 0


def check_all_p(p):
    global_max_solution_count = 0
    max_solution_p_value = 0
    # p will always be even since using odd/even square sum
    for _p in range(2, p, 2):
        local_solution_count = 0
        # max value of a will range in 1 <= a <= p/(2+sqrt(2)) using
        # maxima-minima
        max_a = int(_p / (2 + math.sqrt(2)))
        for a in range(1, max_a):
            if solution_exists(_p, a):
                local_solution_count += 1
        if global_max_solution_count < local_solution_count:
            global_max_solution_count = local_solution_count
            max_solution_p_value = _p
    return max_solution_p_value


if __name__ == '__main__':
    N = input("Enter max value for p : ")
    print "Max no of solution exists for number %d" % (check_all_p(N))
