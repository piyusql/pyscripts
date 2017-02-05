"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 5, 2017

    ProjectEuler Q-14 : longest collatz sequence

    The following iterative sequence is defined for the set of positive integers:

    n => n/2 (n is even)
    n => 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains
    10 terms. Although it has not been proved yet (Collatz Problem), it is thought
    that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    ref : https://projecteuler.net/problem=14

    e.g.
    >>> python q14_longest_collatz_sequence.py
    Enter range of number to check : 10
    Result for number 9 series length is 20
    >>> python q14_longest_collatz_sequence.py
    Enter range of number to check : 100
    Result for number 97 series length is 119
    >>> python q14_longest_collatz_sequence.py
    Enter range of number to check : 1000
    Result for number 871 series length is 179
    >>> python q14_longest_collatz_sequence.py
    Enter range of number to check : 10000
    Result for number 6171 series length is 262
    >>> python q14_longest_collatz_sequence.py
    Enter range of number to check : 100000
    Result for number 77031 series length is 351
    >>> time python q14_longest_collatz_sequence.py
    Enter range of number to check : 1000000
    Result for number 837799 series length is 525

    real    0m28.139s
    user    0m24.631s
    sys     0m0.020s
"""


def series_length(n):
    series = []
    while(n > 1):
        series.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    series.append(n)
    return len(series)


if __name__ == '__main__':
    N = input("Enter range of number to check : ")
    longest_chain = 0, 0
    for number in xrange(1, N):
        check = series_length(number)
        if longest_chain[1] < check:
            longest_chain = number, check
    print "Result for number %d, series length is %d" % longest_chain
