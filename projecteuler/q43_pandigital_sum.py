"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 5, 2017

    ProjectEuler Q-12 : highly divisible triangular number

    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
    we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.

    ref : https://projecteuler.net/problem=43

    e.g:
    >>> time python q43_pandigital_sum.py
    numbers : [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
    sum : 16695334890

    real    0m13.571s
    user    0m13.484s
    sys     0m0.032s
"""

divisor = ((1, 4, 2), (2, 5, 3), (3, 6, 5),
           (4, 7, 7), (5, 8, 11), (6, 9, 13), (7, 10, 17))

from itertools import permutations


def check():
    digits = '0123456789'
    valid_numbers = []
    for num in permutations([d for d in digits], 10):
        number = ''.join(num)
        valid = 1
        for div in divisor:
            if int(number[div[0]:div[1]]) % div[2] != 0:
                valid = 0
        if valid:
            valid_numbers.append(int(number))
    return valid_numbers

if __name__ == '__main__':
    numbers = check()
    print "numbers : %s" % (numbers)
    print "sum : %d" % sum(numbers)
