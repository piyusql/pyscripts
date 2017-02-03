"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 3, 2017

    ProjectEuler Q-52 : min permuted multiples
        when a number id multipled with 2,3,4,5,6
        and the number changes but digits remains same.

    ref : https://projecteuler.net/problem=52

    e.g.
    >>> python q52_peruted_multiples.py
    Enter value for multiples : 1
    Result : 1
    >>> python q52_peruted_multiples.py
    Enter value for multiples : 2
    Result : 125874
    >>> python q52_peruted_multiples.py
    Enter value for multiples : 3
    Result : 142857
    >>> python q52_peruted_multiples.py
    Enter value for multiples : 4
    Result : 142857
    >>> python q52_peruted_multiples.py
    Enter value for multiples : 5
    Result : 142857
    >>> python q52_peruted_multiples.py
    Enter value for multiples : 6
    Result : 142857
"""

from collections import Counter


def check_digits_equality(x, y):
    return Counter(k for k in str(x)) == Counter(k for k in str(y))


def min_permuted_multiples(N):
    num = 1
    while True:
        found = 1
        for i in range(2, N + 1):
            if check_digits_equality(num, num * i):
                continue
            else:
                found = 0
                break
        if found:
            return num
        else:
            num += 1

if __name__ == '__main__':
    N = input("Enter value for multiples : ")
    print "Result : %d" % min_permuted_multiples(N)
