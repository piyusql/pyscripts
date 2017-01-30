"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 30, 2017
    
    ProjectEuler question-1 for generating sum of integers which is
    either divisible by 3 or by 5.
    You will be asked the limit value integer N to calculate sum of.
    It will print the sum of the values filtered dividing by 3 or 5.
    
    e.g.
    python multiple_3or5_sum_1.py
    Enter the limit of N : 10
    23
"""


def main(N):
    return sum([x for x in xrange(N) if ((x % 3) == 0 or (x % 5) == 0)])

if __name__ == '__main__':
    N = input("Enter the limit of N : ")
    print main(N)
