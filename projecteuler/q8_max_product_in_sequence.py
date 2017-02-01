"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 1, 2017

    ProjectEuler Q-8 : finding max product of digits in a given sequence
        of integers and specified choosing sequence_length token.

    ref : https://projecteuler.net/problem=8

    e.g.
    >>> python q8_max_product_in_sequence.py
    Enter the sequence length : 1
    Max product value for 1 consecutive digits : 9
    >>> python q8_max_product_in_sequence.py
    Enter the sequence length : 2
    Max product value for 2 consecutive digits : 81
    >>> python q8_max_product_in_sequence.py
    Enter the sequence length : 3
    Max product value for 3 consecutive digits : 648
    >>> python q8_max_product_in_sequence.py
    Enter the sequence length : 4
    Max product value for 4 consecutive digits : 5832
    >>> python q8_max_product_in_sequence.py
    Enter the sequence length : 13
    Max product value for 13 consecutive digits : 23514624000
"""


from pgmath.prime import nPrime
from functools import reduce
number_series = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""


def find_max_product(number_series, sequence_length):
    valid_series = [
        token for token in number_series.replace(
            '\n',
            '').split(
            '0') if len(
                token) > sequence_length]

    def product(token):
        return reduce(lambda x, y: x * y, [int(i) for i in token])
    all_max = 0
    for each_token in valid_series:
        max_product = max([product(each_token[i:i + sequence_length])
                          for i in xrange(len(each_token) - sequence_length + 1)])
        if all_max < max_product:
            all_max = max_product
    return all_max


if __name__ == '__main__':
    sequence_length = input("Enter the sequence length : ")
    print ("Max product value for %d consecutive digits : %d" %
           (sequence_length, find_max_product(number_series, sequence_length)))
