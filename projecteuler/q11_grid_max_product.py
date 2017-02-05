"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 5, 2017

    ProjectEuler Q-20 : Largest product in a grid
        What is the greatest product of N adjacent numbers
    in the same direction (up, down, left, right, or diagonally)
    in the 20x20 grid ?

    ref : https://projecteuler.net/problem=11

    >>> python q11_grid_max_product.py
    Enter the block size to check in grid : 1
    ((14, 6, (1, 0), (99,)), 99)
    >>> python q11_grid_max_product.py
    Enter the block size to check in grid : 2
    ((1, 2, (-1, 1), (99, 97)), 9603)
    >>> python q11_grid_max_product.py
    Enter the block size to check in grid : 3
    ((14, 4, (-1, 1), (97, 94, 89)), 811502)
    >>> python q11_grid_max_product.py
    Enter the block size to check in grid : 4
    ((15, 3, (-1, 1), (87, 97, 94, 89)), 70600674)
    >>> python q11_grid_max_product.py
    Enter the block size to check in grid : 5
    ((15, 3, (-1, 1), (87, 97, 94, 89, 47)), 3318231678)
    >>> python q11_grid_max_product.py
    Enter the block size to check in grid : 6
    ((4, 9, (-1, 1), (92, 68, 67, 98, 78, 52)), 166607890176)
"""

import operator
from functools import reduce
grid =  """
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """


class Direction():
    # Direction names with their coordinates movement in row, column
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (1, 0)
    DIAGONAL_LEFT_UP = (-1, -1)
    DIAGONAL_LEFT_DOWN = (1, -1)
    DIAGONAL_RIGHT_UP = (-1, 1)
    DIAGONAL_RIGHT_DOWN = (1, 1)


class Grid():

    def __init__(self, text):
        grid2d = []
        for line in text.strip().split('\n'):
            grid2d.append([int(number) for number in line.strip().split()])
        self.grid2d = grid2d
        self.rows = len(grid2d)
        self.columns = len(grid2d[0]) if self.rows else 0

    def product(self, list_of_integers):
        return reduce(lambda x, y: x * y, list_of_integers)

    def find_product_in_direction(self, N, direction):
        # considering the following direction rules, it will ease the no of steps to calculate
        # RIGHT and LEFT direction will result the same set of numbers
        # UP and DOWN direction will result the same set of numbers
        # DIAGONAL_LEFT_UP and DIAGONAL_RIGHT_DOWN will result the same set of
        # numbers
        result = {}
        for i in range(self.rows):
            for j in range(self.columns):
                try:
                    checkset = tuple(self.grid2d[i + direction[0] * k][j + direction[1] * k]
                                     for k in range(N))
                    result[(i, j, direction, checkset)] = self.product(
                        checkset)
                except IndexError:
                    break
        # DIAGONAL_LEFT_DOWN and DIAGONAL_RIGHT_UP will result the same set of
        # numbers
        self.result = max(result.items(), key=operator.itemgetter(1))
        return self.result

if __name__ == '__main__':
    N = input("Enter the block size to check in grid : ")
    gr = Grid(grid)
    print max(
             (gr.find_product_in_direction(N, Direction.RIGHT),
              gr.find_product_in_direction(N, Direction.DOWN),
              gr.find_product_in_direction(N, Direction.DIAGONAL_RIGHT_DOWN),
              gr.find_product_in_direction(N, Direction.DIAGONAL_RIGHT_UP)),
        key=operator.itemgetter(1))
