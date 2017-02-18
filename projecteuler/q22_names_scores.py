"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 18, 2017

    ProjectEuler Q-22 : sum of names scores

    For example,
        when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name
    in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

    ref : https://projecteuler.net/problem=22
    
    >>> time python q22_names_scores.py 
    Sum :  871198282

    real    0m0.191s
    user    0m0.178s
    sys     0m0.012s
"""


def sort_names(_file):
    names = map(lambda x: x.strip('"'), open(_file).read().split(','))
    return sorted(names)


def get_score(name):
    char_sum = sum((ord(c) - 64 for c in name))
    return char_sum * (names.index(name) + 1)

if __name__ == '__main__':
    names = sort_names('p022_names.txt')
    print "Sum : ", sum(map(get_score, names))
