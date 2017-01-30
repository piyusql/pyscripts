"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 30, 2017

    ProjectEuler Q-4 : palindrome with the largest factor of N digit

    ref : https://projecteuler.net/problem=4

    e.g.
    >>> python largest_palindrome_product_q4.py
    Enter the factor digit : 2
    Largest palindrome : 9009 with factors [99, 91]
    >>> python largest_palindrome_product_q4.py
    Enter the factor digit : 3
    Largest palindrome : 906609 with factors [993, 913]
    >>> python largest_palindrome_product_q4.py
    Enter the factor digit : 4
    Largest palindrome : 99000099 with factors [9999, 9901]
    >>> python largest_palindrome_product_q4.py
    Enter the factor digit : 9
    Largest palindrome : 999900665566009999 with factors [999980347, 999920317]
"""


def reverse_int(num):
    # if the last digit is 0 it makes the reverse of digit having n-1 digit
    digits = []
    while(num > 0):
        digits.append(num % 10)
        num = num / 10
    new_num = 0
    for i, _digit in enumerate(digits):
        new_num += _digit * (10 ** (len(digits) - 1 - i))
    return new_num


def reverse(num):
    # str reverse is only capable incase of int 990 --> 099 turns into 99
    return "".join([x for x in num][::-1])


def construct_serial_palindrome(N):
    for i in xrange(1, ((10 ** N) - 10 ** (N - 1))):
        number = (10 ** N) - i
        yield int("%d%s" % (number, reverse(str(number))))


def find_palindrome(N):
    for x in construct_serial_palindrome(N):
        factors = []
        limit = int(x ** 0.5) - 1
        for i in xrange(limit, 10 ** N):
            if x % i == 0 and x / i < 10 ** N:
                factors.append(i)
                factors.append(x / i)
                break
        if factors:
            return x, factors
    return None, None

if __name__ == '__main__':
    N = input("Enter the factor digit : ")
    palindrome, factors = find_palindrome(N)
    if palindrome:
        print "Largest palindrome : %d with factors %s" % (palindrome, factors)
    else:
        print "No palindrome found"
