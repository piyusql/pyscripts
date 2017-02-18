"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 18, 2017

    ProjectEuler Q-18 : maximum path sum while travelling on a triangle to either 1 left or 1 right number

    ref : https://projecteuler.net/problem=18
"""
triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
import sys
from pgmath.factorial import memoize

def parse_triangle(_file):
    return parse_triangle_from_text(open(_file).read())


def parse_triangle_from_text(text):
    lines = text.strip().splitlines()
    last_row_numbers_len = len(lines[-1].split())
    max_index = (last_row_numbers_len - 1) * 2 + 1
    numbers_2d_repr = []
    blank_value = '  '
    for i, line in enumerate(lines):
        each_line = []
        numbers = map(lambda x: int(x), line.split())
        for j in range(last_row_numbers_len - i - 1):
            each_line.append(blank_value)
        for j in numbers[:-1]:
            each_line.append(j)
            each_line.append(blank_value)
        each_line.append(numbers[-1])
        for j in range(last_row_numbers_len - i - 1):
            each_line.append(blank_value)
        numbers_2d_repr.append(each_line)
    return numbers_2d_repr


def simple_parse(text):
    return [map(lambda x: int(x), line.strip().split())
            for line in text.strip().splitlines()]


def simple_parse_from_file(_file):
    return simple_parse(open(_file).read())

@memoize
def get_max_value(line_no, index):
    """
    Simple recursive method to find max sum
    complexity = 2^n where n is no of rows
    """
    global iterations
    iterations += 1
    if line_no == len(numbers) - 1 or index == len(numbers[-1]):
        return numbers[line_no][index]
    return numbers[line_no][index] + max(get_max_value(line_no + 1, index),
                                         get_max_value(line_no + 1, index + 1))

if __name__ == '__main__':
    iterations = 0
    if len(sys.argv) == 2:
        _file = sys.argv[1]
        numbers = simple_parse_from_file(_file)
    else:
        numbers = simple_parse(triangle)
    print "Max Sum : ", get_max_value(0, 0)
    print "Iterations : ", iterations
