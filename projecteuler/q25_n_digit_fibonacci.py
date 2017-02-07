"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 7, 2017

    ProjectEuler Q-25 : finding Nth digit fibonacci series

    ref : https://projecteuler.net/problem=25

    e.g.
    >>> python q25_n_digit_fibonacci.py
    Enter the digit count, N : 10
    Fib index : 45

    >>> python q25_n_digit_fibonacci.py
    Enter the digit count, N : 100
    Fib index : 476

    >>> python q25_n_digit_fibonacci.py
    Enter the digit count, N : 1000
    Fib index : 4782

    real    0m1.920s
    user    0m0.069s
    sys     0m0.005s

    >>> time python q25_n_digit_fibonacci.py
    Enter the digit count, N : 10000
    Fib index : 47847

    real    0m39.507s
    user    0m36.996s
    sys     0m0.080s
"""


def nth_digit_fibonacci(N):
    d = 1
    count = 0
    for f in fib():
        count += 1
        d = len(str(f))
        if d >= N:
            break
    return count


def fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

if __name__ == '__main__':
    N = input("Enter the digit count, N : ")
    print "Fib index : %d" % (nth_digit_fibonacci(N))
