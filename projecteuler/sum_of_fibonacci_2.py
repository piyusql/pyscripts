"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 30, 2017

    ProjectEuler Q-2 for generating sum of even numbers from fibonacci series
    where it starts from 1, 2, 3, 5, 8, 13, 21, ...
    You will be asked the limit value integer N to calculate sum of.
    It will print the sum of the values filtered dividing by 3 or 5.

    ref : https://projecteuler.net/problem=2
    
    e.g.
    python sum_of_fibonacci_2.py
    Enter the limit of N : 4000000
    4613732
"""


def fibonacci(N):
    a = 1
    b = 2
    yield a
    while(b < N):
        yield b
        a, b = b, a + b

if __name__ == '__main__':
    N = input("Enter the limit of N : ")
    print "Sum of even values : %d" % sum(x for x in fibonacci(N) if x % 2 == 0)
