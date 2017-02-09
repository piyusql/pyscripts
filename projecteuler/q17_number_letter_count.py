"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 6, 2017

    ProjectEuler Q-15 : currency number to word conversion

    If the numbers 1 to 5 are written out in words: one, two,
    three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
    letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive
    were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342
    (three hundred and forty-two) contains 23 letters and 115
    (one hundred and fifteen) contains 20 letters. The use of "and"
    when writing out numbers is in compliance with British usage.

    >>> python q17_number_letter_count.py 1
    one
    >>> python q17_number_letter_count.py 12
    twelve
    >>> python q17_number_letter_count.py 123
    one hundred and twenty three
    >>> python q17_number_letter_count.py 1234
    one thousand two hundred and thirty four
    >>> python q17_number_letter_count.py 1239
    one thousand two hundred and thirty nine
    >>> python q17_number_letter_count.py 129
    one hundred and twenty nine
    >>> python q17_number_letter_count.py 19
    nineteen
    >>> python q17_number_letter_count.py
    Total char sum upto 1000 : 21124
"""


SEPARATOR = ' '
ONES = ['', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
HUNDREDS = 'hundred'
THOUSANDS = 'thousand'


class Currency():

    def __init__(self):
        pass

    @staticmethod
    def join(*args):
        return SEPARATOR.join(args)

    @staticmethod
    def trim(strp):
        return SEPARATOR.join(strp.split())

    def number_to_text(self, num):
        num = int(num)
        th, num = num / 1000, num % 1000
        h, num = num / 100, num % 100
        text = ''
        if th:
            text = Currency.join(text, ONES[th], THOUSANDS)
        if h:
            text = Currency.join(text, ONES[h], HUNDREDS, 'and' if num else '')
        if num >= 10 and num < 20:
            text = Currency.join(text, TEENS[num - 10])
        if num >= 20:
            text = Currency.join(text, TENS[num / 10])
        if num < 10 or (num > 20 and num % 10):
            text = Currency.join(text, ONES[num % 10])
        return Currency.trim(text)

if __name__ == '__main__':
    import sys
    cr = Currency()
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        print cr.number_to_text(N)
    else:
        x = 0
        for n in xrange(1, 1001):
            tt = cr.number_to_text(n)
            x += len("".join(tt.split()))
        print "Total char sum upto 1000 : %d" % (x)
