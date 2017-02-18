"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 18, 2017

    ProjectEuler Q-36 : palindromes in double base

    ref : https://projecteuler.net/problem=36

    e.g:
"""


def is_palindrome(num):
    num_str = str(num)
    for i in range(len(num_str) / 2 + len(num_str) % 2):
        if num_str[i] != num_str[-i - 1]:
            return False
    return True


def decimal2binary(num):
    if num == 0:
        return ''
    else:
        return decimal2binary(num / 2) + str(num % 2)


def check(N):
    valid_numbers = []
    for num in xrange(1, N):
        if is_palindrome(num):
            if is_palindrome(decimal2binary(num)):
                valid_numbers.append(num)
    return valid_numbers

if __name__ == '__main__':
    N = input("Enter value for limit : ")
    numbers = check(N)
    print "sum : %d" % sum(numbers)
