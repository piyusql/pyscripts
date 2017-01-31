"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 31, 2017

    ProjectEuler Q-7 : get the Nth term of prime number

    ref : https://projecteuler.net/problem=7

    e.g.
    >>> python q7_next_prime_number.py
    Enter the Nth term N : 1
    1th prime number : 2
    >>> python q7_next_prime_number.py
    Enter the Nth term N : 5
    5th prime number : 11
    >>> python q7_next_prime_number.py
    Enter the Nth term N : 10
    10th prime number : 29
    >>> python q7_next_prime_number.py
    Enter the Nth term N : 25
    25th prime number : 97
    >>> python q7_next_prime_number.py
    Enter the Nth term N : 10001
    10001th prime number : 104743
"""


from pgmath.prime import nPrime

if __name__ == '__main__':
    N = input("Enter the Nth term N : ")
    for prime in nPrime(N):
        # iterate till last and return the largest value
        pass
    print "%dth prime number : %d" % (N, prime)
