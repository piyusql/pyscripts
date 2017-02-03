"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 3, 2017

    ProjectEuler Q-35 : finding the prime numbers whose all rotations
        are also primme values

    ref : https://projecteuler.net/problem=35

    e.g.
    >>> python q35_circular_primes.py
    Enter range value for primes : 100
    Total Count : 13
    >>> python q35_circular_primes.py
    Enter range value for primes : 1000
    Total Count : 25
    >>> python q35_circular_primes.py
    Enter range value for primes : 100000
    Total Count : 43
    >>> python q35_circular_primes.py
    Enter range value for primes : 1000000
    Total Count : 55
"""
from pgmath.prime import primeTillN


def circular_primes(N):
    circular_prime_list = []
    primes = [prime for prime in primeTillN(N)]
    rotation = lambda num_str: sorted(
        [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))])
    for prime in primes:
        for prime2 in rotation(str(prime)):
            circular = 1
            if prime2 in primes:
                continue
            else:
                circular = 0
                break
        if circular:
            circular_prime_list.append(prime)
        # all rotation primes checked
    return circular_prime_list

if __name__ == '__main__':
    N = input("Enter range value for primes : ")
    nums = circular_primes(N)
    print "Total Count : %d" % len(nums)
