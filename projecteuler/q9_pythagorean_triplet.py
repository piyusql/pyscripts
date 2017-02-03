"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 2, 2017

    ProjectEuler Q-9 : finding pythagorean triplet where
        a + b + c = 1000 and a^2 + b^2 = c^2
        e.g a=3, b=4, c = 5, another one exists within 1000
    idea to solve this question is that if the perimeter of a triangle
    is N(a+b+c) then each of its side will always be less than N/2.

    ref : https://projecteuler.net/problem=9

    e.g.
    >>> python q9_pythagorean_triplet.py
    Enter value for a+b+c : 10
    No such pythagorean found where a+b+c=10
    >>> python q9_pythagorean_triplet.py
    Enter value for a+b+c : 12
    Numbers : 3, 4, 5, Product : 60
    >>> python q9_pythagorean_triplet.py
    Enter value for a+b+c : 100
    No such pythagorean found where a+b+c=100
    >>> python q9_pythagorean_triplet.py
    Enter value for a+b+c : 1000
    Numbers : 200, 375, 425, Product : 31875000
"""


def find_pythagorean(N):
    check_pythagorean = lambda x, y, z: (x ** 2) + (y ** 2) == (z ** 2)
    for a in xrange(1, N / 2):
        for b in xrange(1, N / 2):
            for c in xrange(1, N / 2):
                # check the sum first to do smaller calculation
                if (a + b + c) == N and check_pythagorean(a, b, c):
                    return a, b, c
    # all check for triangle side size N/2 checked
    return

if __name__ == '__main__':
    N = input("Enter value for a+b+c : ")
    result = find_pythagorean(N)
    if result:
        a, b, c = result
        print "Numbers : %d, %d, %d, Product : %d" % (a, b, c, a * b * c)
    else:
        print "No such pythagorean found where a+b+c=%d" % (N)
