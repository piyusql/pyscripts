"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 6, 2017

    ProjectEuler Q-21 : Amicable numbers pairs

    ref : https://projecteuler.net/problem=21

    Let d(n) be defined as the sum of proper divisors of n
        (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an
        amicable pair and each of a and b are called amicable numbers.

    For example,
        the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
        therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
        so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

    e.g.
    >>> python q21_amicable_numbers.py
    Enter the range to check and sum, N : 100
    Sum of amicable pairs with in 100 is : 0

    >>> python q21_amicable_numbers.py
    Enter the range to check and sum, N : 123
    Sum of amicable pairs with in 123 is : 0

    >>> python q21_amicable_numbers.py
    Enter the range to check and sum, N : 1000
    Sum of amicable pairs with in 1000 is : 504

    >>> python q21_amicable_numbers.py
    Enter the range to check and sum, N : 10000
    Sum of amicable pairs with in 10000 is : 31626
"""


from pgmath.factorial import factorial, factorial1


def sum_divisors(n):
    divisors = [1]
    for d in xrange(2, n):
        if n % d == 0:
            divisors.append(d)
    return sum(divisors)

if __name__ == '__main__':
    N = input("Enter the range to check and sum, N : ")
    amicable_pairs = []
    for n in xrange(2, N):
        a = sum_divisors(n)
        b = sum_divisors(a)
        if b == n and a != b:
            amicable_pairs.append(n)
    print "Sum of amicable pairs with in %d is : %d" % (N, sum(amicable_pairs))
