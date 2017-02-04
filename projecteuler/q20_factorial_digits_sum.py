"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 4, 2017

    ProjectEuler Q-20 : sum of digits of factorial of N

    ref : https://projecteuler.net/problem=20

    e.g.
    >>> python q20_factorial_digits_sum.py
    Enter the integer value N : 1
    1! = 1
    Sum of digits : 1
    >>> python q20_factorial_digits_sum.py
    Enter the integer value N : 10
    10! = 3628800
    Sum of digits : 27
    >>> python q20_factorial_digits_sum.py
    Enter the integer value N : 100
    100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    Sum of digits : 648
"""


from pgmath.factorial import factorial, factorial1


if __name__ == '__main__':
    N = input("Enter the integer value N : ")
    number = factorial1(N)
    print "%d! = %d" % (N, number)
    print "Sum of digits : %d" % sum(int(d) for d in str(number))
