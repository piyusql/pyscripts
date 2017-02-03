"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 3, 2017

    ProjectEuler Q-30 : finding the numbers which is equal to
        the sum of nth power of the all digits in that number.

    ref : https://projecteuler.net/problem=30

    e.g.
    >>> python q30_digit_nth_power_sum.py
    Enter value for power : 1
    Numbers : [2, 3, 4, 5, 6, 7, 8, 9], Sum : 44
    >>> python q30_digit_nth_power_sum.py
    Enter value for power : 2
    Numbers : [], Sum : 0
    >>> python q30_digit_nth_power_sum.py
    Enter value for power : 3
    Numbers : [153, 370, 371, 407], Sum : 1301
    >>> python q30_digit_nth_power_sum.py
    Enter value for power : 4
    Numbers : [1634, 8208, 9474], Sum : 19316
    >>> python q30_digit_nth_power_sum.py
    Enter value for power : 5
    Numbers : [4150, 4151, 54748, 92727, 93084, 194979], Sum : 443839
"""


def find_numbers(N):
    numbers = []
    # since the sum of 5th powers of digit will always be within 6 digits
    for num in xrange(2, 10 ** (N + 1)):
        if num == sum(int(d) ** N for d in str(num)):
            numbers.append(num)
    return numbers

if __name__ == '__main__':
    N = input("Enter value for power : ")
    numbers = find_numbers(N)
    print "Numbers : %s, Sum : %d" % (numbers, sum(numbers))
