"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 18, 2017

    ProjectEuler Q-24 : lexicographic permutations



    A permutation is an ordered arrangement of objects.
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
    If all of the permutations are listed numerically or alphabetically, we call
    it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
        012   021   102   120   201   210
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

    ref : https://projecteuler.net/problem=24

"""


from itertools import permutations

if __name__ == '__main__':
    chars = '0123456789'
    # without sorting also permutations gives result in given chars order
    print sorted(map(lambda x: int("".join(x)), permutations(chars)))[1000000 - 1]
    print "".join(list(permutations(chars))[1000000 - 1])
