"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 1, 2017

    ProjectEuler Q-10 : finding sun of prime number within a given range N

    ref : https://projecteuler.net/problem=10

    e.g.
    >>> python q10_sum_of_primes.py
    Enter the range value N : 10
    Sum of prime till 10 is 17
    >>> python q10_sum_of_primes.py
    Enter the range value N : 100
    Sum of prime till 100 is 1060
    >>> python q10_sum_of_primes.py
    Enter the range value N : 1000
    Sum of prime till 1000 is 76127
    >>> python q10_sum_of_primes.py
    Enter the range value N : 100000
    Sum of prime till 100000 is 454396537
    >>> python q10_sum_of_primes.py
    Enter the range value N : 2000000
    Sum of prime till 2000000 is 142913828922
"""


from pgmath.prime import primeTillN


if __name__ == '__main__':
    N = input("Enter the range value N : ")
    prime_sum = 0
    for prime in primeTillN(N):
        prime_sum += prime
    print "Sum of prime till %d is %d" % (N, prime_sum)
