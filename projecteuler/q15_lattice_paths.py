"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Feb 6, 2017

    ProjectEuler Q-15 : lattice paths counting routes

    Starting in the top left corner of a 2x2 grid, and only being
    able to move to the right and down, there are exactly 6 routes
    to the bottom right corner.

    How many such routes are there through a 20x20 grid?

    >>> python q15_lattice_paths.py
    Enter no of rows : 2
    Enter no of columns : 2
    Route count from start to end : 6
    >>> python q15_lattice_paths.py
    Enter no of rows : 20
    Enter no of columns : 20
    Route count from start to end : 137846528820
"""


class Grid():

    def __init__(self, rows, columns):
        # since we are making a grid and wanted to count path
        # so for each rows and columns it will need 1 more dot to connect
        self.rows = rows + 1
        self.columns = columns + 1
        self.grid2d = [[None for i in range(self.columns)]
                       for j in range(self.rows)]

    def find_possible_paths(self):
        # filling the first row with 1, all point can be reached in a single
        # way towards right
        for i in range(self.columns):
            self.grid2d[0][i] = 1
        # filling the first column with 1, all points can be reached in a
        # single way towards down
        for j in range(self.rows):
            self.grid2d[j][0] = 1
        for i in range(1, self.rows):
            for j in range(1, self.columns):
                self.grid2d[i][j] = self.grid2d[
                    i - 1][j] + self.grid2d[i][j - 1]

if __name__ == '__main__':
    N = input("Enter no of rows : ")
    M = input("Enter no of columns : ")
    gr = Grid(N, M)
    gr.find_possible_paths()
    print "Route count from start to end : %s" % (gr.grid2d[-1][-1])
